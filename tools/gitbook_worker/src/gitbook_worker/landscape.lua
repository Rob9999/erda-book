function Div(el)
  if el.classes:includes('landscape') then
    if FORMAT:match('latex') then
      local blocks = {pandoc.RawBlock('latex', '\\begin{landscape}')}
      for _, b in ipairs(el.content) do
        table.insert(blocks, b)
      end
      table.insert(blocks, pandoc.RawBlock('latex', '\\end{landscape}'))
      return blocks
    else
      return el.content
    end
  end
end
