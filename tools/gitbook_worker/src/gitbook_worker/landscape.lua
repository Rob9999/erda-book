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
    -- 1) Landscape-Umgebung
    table.insert(blocks, pandoc.RawBlock('latex', '\\begin{landscape}'))
    -- 2) Schmalere Ränder
    table.insert(blocks, pandoc.RawBlock('latex', '\\newgeometry{margin=1cm,landscape}'))
    -- 3) adjustbox
    table.insert(blocks, pandoc.RawBlock('latex',
      '\\begin{adjustbox}{max width=\\linewidth,center}'))
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
    -- 7) Ränder wiederherstellen
    table.insert(blocks, pandoc.RawBlock('latex', '\\restoregeometry'))
    -- 8) Landscape beenden
    table.insert(blocks, pandoc.RawBlock('latex', '\\end{landscape}'))

    return blocks
  end
  return nil
end