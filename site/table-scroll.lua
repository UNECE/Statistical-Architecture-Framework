-- Wrap every table in a <div class="table-scroll"> (HTML only), so a wide
-- table scrolls inside its own box instead of running under the margin TOC.
-- Styled in custom.scss (.table-scroll).
if not quarto.doc.is_format("html") then
  return {}
end

function Table(tbl)
  return pandoc.Div({ tbl }, pandoc.Attr("", { "table-scroll" }))
end
