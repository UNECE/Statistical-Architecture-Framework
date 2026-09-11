-- Cross-document links are written as `.qmd` so the HTML site resolves them.
-- Quarto does not rewrite them for PDF, which leaves dead `.qmd` targets in the
-- PDF. Point them at the rendered `.html` instead, and make them absolute when
-- `pdf-link-base` is set in the metadata.
local base = nil

function Meta(m)
  if m["pdf-link-base"] then base = pandoc.utils.stringify(m["pdf-link-base"]) end
end

function Link(el)
  local t = el.target
  if t:match("^%a[%w+.-]*:") or t:match("^#") or t:match("^//") then
    return el                      -- external URL, mailto, or same-page anchor
  end
  t = t:gsub("%.qmd", ".html")
  if base and not t:match("^/") then
    t = base:gsub("/$", "") .. "/" .. t
  end
  el.target = t
  return el
end
