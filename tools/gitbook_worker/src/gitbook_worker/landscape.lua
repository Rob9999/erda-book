function Div(el)
  if FORMAT:match('latex') and el.classes:includes('landscape') then
    local cols = tonumber(el.attributes['cols']) or 0
    -- Schriftgröße wählen
    local size = ''
    if cols >= 13 then
      size = '\\tiny'
    elseif cols >= 10 then
      size = '\\scriptsize'
    elseif cols >= 7 then
      size = '\\footnotesize'
    end

    local blocks = {}
    local contains_table = false
    for _, b in ipairs(el.content) do
      if b.t == 'Table' then
        contains_table = true
        break
      end
    end

    local use_longtable = contains_table and PANDOC_WRITER_OPTIONS and PANDOC_WRITER_OPTIONS.longtable

    -- 1) Landscape-Umgebung
    table.insert(blocks, pandoc.RawBlock('latex', '\\begin{landscape}'))
    -- 2) Schmalere Ränder
    table.insert(blocks, pandoc.RawBlock('latex', '\\newgeometry{margin=1cm,landscape}'))

    if use_longtable then
      -- longtable kann nicht in adjustbox gesetzt werden -> ltablex nutzen
      if size ~= '' then
        table.insert(blocks, pandoc.RawBlock('latex', '\\begingroup' .. size))
      end
      local doc = pandoc.Pandoc(el.content)
      local latex = pandoc.write(doc, 'latex', PANDOC_WRITER_OPTIONS)
      latex = latex:gsub('\\begin{longtable}', '\\begin{ltablex}{\\linewidth}')
      latex = latex:gsub('\\end{longtable}', '\\end{ltablex}')
      table.insert(blocks, pandoc.RawBlock('latex', latex))
      if size ~= '' then
        table.insert(blocks, pandoc.RawBlock('latex', '\\endgroup'))
      end
    else
      -- 3) adjustbox
      table.insert(blocks, pandoc.RawBlock('latex', '\\begin{adjustbox}{max width=\\linewidth,center}'))
      -- 4) Gruppierung & Schriftgröße
      if size ~= '' then
        table.insert(blocks, pandoc.RawBlock('latex', '\\begingroup' .. size))
      end
      -- 5) Original-Inhalt
      for _, b in ipairs(el.content) do
        table.insert(blocks, b)
      end
      -- 6) Endgroup & adjustbox schließen
      if size ~= '' then
        table.insert(blocks, pandoc.RawBlock('latex', '\\endgroup'))
      end
      table.insert(blocks, pandoc.RawBlock('latex', '\\end{adjustbox}'))
    end

    -- 7) Ränder wiederherstellen
    table.insert(blocks, pandoc.RawBlock('latex', '\\restoregeometry'))
    -- 8) Landscape beenden
    table.insert(blocks, pandoc.RawBlock('latex', '\\end{landscape}'))

    return blocks
  end
  return nil
end
