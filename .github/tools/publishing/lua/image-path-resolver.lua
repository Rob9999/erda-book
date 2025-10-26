-- image-path-resolver.lua
-- This filter ensures proper resolution of image paths from .gitbook/assets

local function resolve_image(img)
    -- Get the image path
    local src = img.src or ""
    
    -- Check if the path is relative and points to .gitbook/assets
    if not src:match("^https?://") and not src:match("^/") then
        -- Try to resolve relative to .gitbook/assets first
        local gitbook_path = ".gitbook/assets/" .. src
        if os.execute('test -f "' .. gitbook_path .. '"') then
            img.src = gitbook_path
        end
    end
    
    return img
end

return {
    {
        Image = resolve_image
    }
}