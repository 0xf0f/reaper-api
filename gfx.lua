-- REAPER 5.95


local original_gfx = gfx
local gfx = {}


---gfx.r, gfx.g, gfx.b, gfx.a - These represent the current red, green, blue, and alpha components used by drawing operations (0.0..1.0).
gfx.r = nil


---gfx.r, gfx.g, gfx.b, gfx.a - These represent the current red, green, blue, and alpha components used by drawing operations (0.0..1.0).
gfx.g = nil


---gfx.r, gfx.g, gfx.b, gfx.a - These represent the current red, green, blue, and alpha components used by drawing operations (0.0..1.0).
gfx.b = nil


---gfx.r, gfx.g, gfx.b, gfx.a - These represent the current red, green, blue, and alpha components used by drawing operations (0.0..1.0).
gfx.a = nil


---gfx.w, gfx.h - These are set to the current width and height of the UI framebuffer.
gfx.w = nil


---gfx.w, gfx.h - These are set to the current width and height of the UI framebuffer.
gfx.h = nil


---gfx.x, gfx.y - These set the "current" graphics position in x,y. You can set these yourselves, and many of the drawing functions update them as well.
gfx.x = nil


---gfx.x, gfx.y - These set the "current" graphics position in x,y. You can set these yourselves, and many of the drawing functions update them as well.
gfx.y = nil


---Set to 0 for default options. Add 1.0 for additive blend mode (if you wish to do subtractive, set gfx.a to negative and use gfx.mode as additive). Add 2.0 to disable source alpha for gfx.blit(). Add 4.0 to disable filtering for gfx.blit().
gfx.mode = nil


---If set to a value greater than -1.0, this will result in the framebuffer being cleared to that color. the color for this one is packed RGB (0..255), i.e. red+green*256+blue*65536. The default is 0 (black).
gfx.clear = nil


---Defaults to -1, set to 0..1024-1 to have drawing operations go to an offscreen buffer (or loaded image).
gfx.dest = nil


---Set to the height of a line of text in the current font. Do not modify this variable.
gfx.texth = nil


---If set to 1.0 on initialization, will be updated to 2.0 if high resolution display is supported, and if so gfx.w/gfx.h/etc will be doubled.
gfx.ext_retina = nil


---gfx.mouse_x, gfx.mouse_y - gfx.mouse_x and gfx.mouse_y are set to the coordinates of the mouse relative to the graphics window.
gfx.mouse_x = nil


---gfx.mouse_x, gfx.mouse_y - gfx.mouse_x and gfx.mouse_y are set to the coordinates of the mouse relative to the graphics window.
gfx.mouse_y = nil


---gfx.mouse_wheel, gfx.mouse_hwheel - mouse wheel (and horizontal wheel) positions. These will change typically by 120 or a multiple thereof, the caller should clear the state to 0 after reading it.
gfx.mouse_wheel = nil


---gfx.mouse_wheel, gfx.mouse_hwheel - mouse wheel (and horizontal wheel) positions. These will change typically by 120 or a multiple thereof, the caller should clear the state to 0 after reading it.
gfx.mouse_hwheel = nil


---is a bitfield of mouse and keyboard modifier state.1: left mouse button2: right mouse button4: Control key8: Shift key16: Alt key32: Windows key64: middle mouse button
gfx.mouse_cap = nil


---Lua: gfx.arc(x,y,r,ang1,ang2[,antialias])
---
---Draws an arc of the circle centered at x,y, with ang1/ang2 being specified in radians.
function gfx.arc(x, y, r, ang1, ang2, antialias)
end


---Lua: gfx.blit(source, scale, rotation[, srcx, srcy, srcw, srch, destx, desty, destw, desth, rotxoffs, rotyoffs])
---
---srcx/srcy/srcw/srch specify the source rectangle (if omitted srcw/srch default to image size), destx/desty/destw/desth specify dest rectangle (if not specified, these will default to reasonable defaults -- destw/desth default to srcw/srch * scale).
function gfx.blit(source, scale, rotation, srcx, srcy, srcw, srch, destx, desty, destw, desth, rotxoffs, rotyoffs)
end


---Lua: gfx.blit(source, scale, rotation[, srcx, srcy, srcw, srch, destx, desty, destw, desth, rotxoffs, rotyoffs])
---
---srcx/srcy/srcw/srch specify the source rectangle (if omitted srcw/srch default to image size), destx/desty/destw/desth specify dest rectangle (if not specified, these will default to reasonable defaults -- destw/desth default to srcw/srch * scale).
function gfx.blit(source, scale, rotation, srcx, srcy, srcw, srch, destx, desty, destw, desth, rotxoffs, rotyoffs)
end


---Lua: gfx.blitext(source,coordinatelist,rotation)
---
---Deprecated, use gfx.blit instead.
function gfx.blitext(source, coordinatelist, rotation)
end


---Lua: gfx.blurto(x,y)
---
---Blurs the region of the screen between gfx.x,gfx.y and x,y, and updates gfx.x,gfx.y to x,y.
function gfx.blurto(x, y)
end


---Lua: gfx.circle(x,y,r[,fill,antialias])
---
---Draws a circle, optionally filling/antialiasing.
function gfx.circle(x, y, r, fill, antialias)
end


---Lua: gfx.clienttoscreen(x,y)
---
---Converts the coordinates x,y to screen coordinates, returns those values.
function gfx.clienttoscreen(x, y)
end


---Lua: gfx.deltablit(srcimg,srcs,srct,srcw,srch,destx,desty,destw,desth,dsdx,dtdx,dsdy,dtdy,dsdxdy,dtdxdy[,usecliprect=1])
---
---Blits from srcimg(srcx,srcy,srcw,srch) to destination (destx,desty,destw,desth). Source texture coordinates are s/t, dsdx represents the change in s coordinate for each x pixel, dtdy represents the change in t coordinate for each y pixel, etc. dsdxdy represents the change in dsdx for each line. If usecliprect is specified and 0, then srcw/srch are ignored.
function gfx.deltablit(srcimg, srcs, srct, srcw, srch, destx, desty, destw, desth, dsdx, dtdx, dsdy, dtdy, dsdxdy, dtdxdy, usecliprect)
end


---Lua: gfx.dock(v[,wx,wy,ww,wh])
---
---Call with v=-1 to query docked state, otherwise v>=0 to set docked state. State is &1 if docked, second byte is docker index (or last docker index if undocked). If wx-wh specified, additional values will be returned with the undocked window position/size
function gfx.dock(v, wx, wy, ww, wh)
end


---Lua: gfx.drawchar(char)
---
---Draws the character (can be a numeric ASCII code as well), to gfx.x, gfx.y, and moves gfx.x over by the size of the character.
function gfx.drawchar(char)
end


---Lua: gfx.drawnumber(n,ndigits)
---
---Draws the number n with ndigits of precision to gfx.x, gfx.y, and updates gfx.x to the right side of the drawing. The text height is gfx.texth.
function gfx.drawnumber(n, ndigits)
end


---Lua: gfx.drawstr("str"[,flags,right,bottom])
---
---Draws a string at gfx.x, gfx.y, and updates gfx.x/gfx.y so that subsequent draws will occur in a similar place.
---If flags, right ,bottom passed in:flags&1: center horizontallyflags&2: right justifyflags&4: center verticallyflags&8: bottom justify
function gfx.drawstr(str, flags, right, bottom)
end


---Lua: gfx.getchar([char])
---
---If char is 0 or omitted, returns a character from the keyboard queue, or 0 if no character is available, or -1 if the graphics window is not open. If char is specified and nonzero, that character's status will be checked, and the function will return greater than 0 if it is pressed.
---Common values are standard ASCII, such as 'a', 'A', '=' and '1', but for many keys multi-byte values are used, including 'home', 'up', 'down', 'left', 'rght', 'f1'.. 'f12', 'pgup', 'pgdn', 'ins', and 'del'.
---Modified and special keys can also be returned, including:Ctrl/Cmd+A..Ctrl+Z as 1..26Ctrl/Cmd+Alt+A..Z as 257..282Alt+A..Z as 'A'+256..'Z'+25627 for ESC13 for Enter' ' for space65536 for query of special flags, returns: &1 (supported), &2=window has focus, &4=window is visible
function gfx.getchar(char)
end


---Lua: gfx.getdropfile(idx)
---
---Returns success,string for dropped file index idx. call gfx.dropfile(-1) to clear the list when finished.
function gfx.getdropfile(idx)
end


---Lua: gfx.getfont()
---
---Returns current font index, and the actual font face used by this font (if available).
function gfx.getfont()
end


---Lua: gfx.getimgdim(handle)
---
---Retreives the dimensions of an image specified by handle, returns w, h pair.
function gfx.getimgdim(handle)
end


---Lua: gfx.getpixel()
---
---Returns r,g,b values [0..1] of the pixel at (gfx.x,gfx.y)
function gfx.getpixel()
end


---Lua: gfx.gradrect(x,y,w,h, r,g,b,a[, drdx, dgdx, dbdx, dadx, drdy, dgdy, dbdy, dady])
---
---Fills a gradient rectangle with the color and alpha specified. drdx-dadx reflect the adjustment (per-pixel) applied for each pixel moved to the right, drdy-dady are the adjustment applied for each pixel moved toward the bottom. Normally drdx=adjustamount/w, drdy=adjustamount/h, etc.
function gfx.gradrect(x, y, w, h, r, g, b, a, drdx, dgdx, dbdx, dadx, drdy, dgdy, dbdy, dady)
end


---Lua: gfx.init("name"[,width,height,dockstate,xpos,ypos])
---
---Initializes the graphics window with title name. Suggested width and height can be specified.
---Once the graphics window is open, gfx.update() should be called periodically.
function gfx.init(name, width, height, dockstate, xpos, ypos)
end


---Lua: gfx.line(x,y,x2,y2[,aa])
---
---Draws a line from x,y to x2,y2, and if aa is not specified or 0.5 or greater, it will be antialiased.
function gfx.line(x, y, x2, y2, aa)
end


---Lua: gfx.lineto(x,y[,aa])
---
---Draws a line from gfx.x,gfx.y to x,y. If aa is 0.5 or greater, then antialiasing is used. Updates gfx.x and gfx.y to x,y.
function gfx.lineto(x, y, aa)
end


---Lua: gfx.loadimg(image,"filename")
---
---Load image from filename into slot 0..1024-1 specified by image. Returns the image index if success, otherwise -1 if failure. The image will be resized to the dimensions of the image file.
function gfx.loadimg(image, filename)
end


---Lua: gfx.measurechar(char)
---
---Measures the drawing dimensions of a character with the current font (as set by gfx.setfont). Returns width and height of character.
function gfx.measurechar(char)
end


---Lua: gfx.measurestr("str")
---
---Measures the drawing dimensions of a string with the current font (as set by gfx.setfont). Returns width and height of string.
function gfx.measurestr(str)
end


---Lua: gfx.muladdrect(x,y,w,h,mul_r,mul_g,mul_b[,mul_a,add_r,add_g,add_b,add_a])
---
---Multiplies each pixel by mul_* and adds add_*, and updates in-place. Useful for changing brightness/contrast, or other effects.
function gfx.muladdrect(x, y, w, h, mul_r, mul_g, mul_b, mul_a, add_r, add_g, add_b, add_a)
end


---Lua: gfx.printf("format"[, ...])
---
---Formats and draws a string at gfx.x, gfx.y, and updates gfx.x/gfx.y accordingly (the latter only if the formatted string contains newline). For more information on format strings, see sprintf()
function gfx.printf(format, ...)
end


---Lua: gfx.quit()
---
---Closes the graphics window.
function gfx.quit()
end


---Lua: gfx.rect(x,y,w,h[,filled])
---
---Fills a rectangle at x,y, w,h pixels in dimension, filled by default.
function gfx.rect(x, y, w, h, filled)
end


---Lua: gfx.rectto(x,y)
---
---Fills a rectangle from gfx.x,gfx.y to x,y. Updates gfx.x,gfx.y to x,y.
function gfx.rectto(x, y)
end


---Lua: gfx.roundrect(x,y,w,h,radius[,antialias])
---
---Draws a rectangle with rounded corners.
function gfx.roundrect(x, y, w, h, radius, antialias)
end


---Lua: gfx.screentoclient(x,y)
---
---Converts the screen coordinates x,y to client coordinates, returns those values.
function gfx.screentoclient(x, y)
end


---Lua: gfx.set(r[,g,b,a,mode,dest])
---
---Sets gfx.r/gfx.g/gfx.b/gfx.a/gfx.mode, sets gfx.dest if final parameter specified
function gfx.set(r, g, b, a, mode, dest)
end


---Lua: gfx.setcursor(resource_id,custom_cursor_name)
---
---Sets the mouse cursor. resource_id is a value like 32512 (for an arrow cursor), custom_cursor_name is a string like "arrow" (for the REAPER custom arrow cursor). resource_id must be nonzero, but custom_cursor_name is optional.
function gfx.setcursor(resource_id, custom_cursor_name)
end


---Lua: gfx.setfont(idx[,"fontface", sz, flags])
---
---Can select a font and optionally configure it. idx=0 for default bitmapped font, no configuration is possible for this font. idx=1..16 for a configurable font, specify fontface such as "Arial", sz of 8-100, and optionally specify flags, which is a multibyte character, which can include 'i' for italics, 'u' for underline, or 'b' for bold. These flags may or may not be supported depending on the font and OS. After calling gfx.setfont(), gfx.texth may be updated to reflect the new average line height.
function gfx.setfont(idx, fontface, sz, flags)
end


---Lua: gfx.setimgdim(image,w,h)
---
---Resize image referenced by index 0..1024-1, width and height must be 0-2048. The contents of the image will be undefined after the resize.
function gfx.setimgdim(image, w, h)
end


---Lua: gfx.setpixel(r,g,b)
---
---Writes a pixel of r,g,b to gfx.x,gfx.y.
function gfx.setpixel(r, g, b)
end


---Lua: gfx.showmenu("str")
---
---Shows a popup menu at gfx.x,gfx.y. str is a list of fields separated by | characters. Each field represents a menu item.
---Fields can start with special characters:
---# : grayed out
---! : checked
---> : this menu item shows a submenu
---< : last item in the current submenu
---An empty field will appear as a separator in the menu. gfx.showmenu returns 0 if the user selected nothing from the menu, 1 if the first field is selected, etc.
---Example:
---gfx.showmenu("first item, followed by separator||!second item, checked|>third item which spawns a submenu|#first item in submenu, grayed out|<second and last item in submenu|fourth item in top menu")
function gfx.showmenu(str)
end


---Lua: gfx.transformblit(srcimg,destx,desty,destw,desth,div_w,div_h,table)
---
---Blits to destination at (destx,desty), size (destw,desth). div_w and div_h should be 2..64, and table should point to a table of 2*div_w*div_h values (table can be a regular table or (for less overhead) a reaper.array). Each pair in the table represents a S,T coordinate in the source image, and the table is treated as a left-right, top-bottom list of texture coordinates, which will then be rendered to the destination.
function gfx.transformblit(srcimg, destx, desty, destw, desth, div_w, div_h, table)
end


---Lua: gfx.triangle(x1,y1,x2,y2,x3,y3[x4,y4...])
---
---Draws a filled triangle, or any convex polygon.
function gfx.triangle(x1, y1, x2, y2, x3, y3, x4, y4, ...)
end


---Lua: gfx.update()
---
---Updates the graphics display, if opened
function gfx.update()
end



gfx = {}
setmetatable(gfx, {
    __index = function(table, key)
        return original_gfx[key]
    end,

    __newindex = function(table, key, value)
        original_gfx[key] = value
    end
})


return gfx
