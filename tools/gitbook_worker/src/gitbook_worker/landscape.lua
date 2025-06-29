function Div(el)
  if el.classes:includes('landscape') then
    if FORMAT:match('latex') then
      local cols = tonumber(el.attributes['cols']) or 0
      local size = ''
      if cols >= 13 then
        size = '\\tiny'
      elseif cols >= 10 then
        size = '\\scriptsize'
      elseif cols >= 7 then
        size = '\\footnotesize'
      end
      local begin_block = '\\begin{landscape}'
      local end_block = '\\end{landscape}'
      if size ~= '' then
        begin_block = begin_block .. '\\begingroup' .. size
        end_block = '\\endgroup' .. end_block
      end
      local blocks = {pandoc.RawBlock('latex', begin_block)}
      for _, b in ipairs(el.content) do
        table.insert(blocks, b)
      end
      table.insert(blocks, pandoc.RawBlock('latex', end_block))
      return blocks
    else
      return el.content
    end
  end
end
