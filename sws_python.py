# SWS 2.9.7


from reaper_python import *
 
def BR_EnvAlloc(envelope,takeEnvelopesUseProjectTime):
    """
    Python: BR_Envelope  BR_EnvAlloc(TrackEnvelope envelope, Boolean takeEnvelopesUseProjectTime)
    
    [BR] Allocate envelope object from track or take envelope pointer. Always call BR_EnvFree
     when done to release the object and commit changes if needed.
    
     takeEnvelopesUseProjectTime: take envelope points' positions are counted from take position, not project start time. If you want to work with project time instead, pass this as true.
    
    
    For further manipulation see BR_EnvCountPoints
    , BR_EnvDeletePoint
    , BR_EnvFind
    , BR_EnvFindNext
    , BR_EnvFindPrevious
    , BR_EnvGetParentTake
    , BR_EnvGetParentTrack
    , BR_EnvGetPoint
    , BR_EnvGetProperties
    , BR_EnvSetPoint
    , BR_EnvSetProperties
    , BR_EnvValueAtPos
    .
    """
    a=rpr_getfp('BR_EnvAlloc')
    f=CFUNCTYPE(c_uint64,c_uint64,c_byte)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_byte(takeEnvelopesUseProjectTime))
    r=f(t[0],t[1])
    return rpr_unpackp('BR_Envelope*',r)
     
def BR_EnvCountPoints(envelope):
    """
    Python: Int  BR_EnvCountPoints(BR_Envelope envelope)
    
    [BR] Count envelope points in the envelope object allocated with BR_EnvAlloc
    .
    """
    a=rpr_getfp('BR_EnvCountPoints')
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('BR_Envelope*',envelope),)
    r=f(t[0])
    return r
     
def BR_EnvDeletePoint(envelope,Id):
    """
    Python: Boolean  BR_EnvDeletePoint(BR_Envelope envelope, Int id)
    
    [BR] Delete envelope point by index (zero-based) in the envelope object allocated with BR_EnvAlloc
    . Returns true on success.
    """
    a=rpr_getfp('BR_EnvDeletePoint')
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_int(Id))
    r=f(t[0],t[1])
    return r
     
def BR_EnvFind(envelope,position,delta):
    """
    Python: Int  BR_EnvFind(BR_Envelope envelope, Float position, Float delta)
    
    [BR] Find envelope point at time position in the envelope object allocated with BR_EnvAlloc
    . Pass delta > 0 to search surrounding range - in that case the closest point to position within delta will be searched for. Returns envelope point id (zero-based) on success or -1 on failure.
    """
    a=rpr_getfp('BR_EnvFind')
    f=CFUNCTYPE(c_int,c_uint64,c_double,c_double)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_double(position),c_double(delta))
    r=f(t[0],t[1],t[2])
    return r
     
def BR_EnvFindNext(envelope,position):
    """
    Python: Int  BR_EnvFindNext(BR_Envelope envelope, Float position)
    
    [BR] Find next envelope point after time position in the envelope object allocated with BR_EnvAlloc
    . Returns envelope point id (zero-based) on success or -1 on failure.
    """
    a=rpr_getfp('BR_EnvFindNext')
    f=CFUNCTYPE(c_int,c_uint64,c_double)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_double(position))
    r=f(t[0],t[1])
    return r
     
def BR_EnvFindPrevious(envelope,position):
    """
    Python: Int  BR_EnvFindPrevious(BR_Envelope envelope, Float position)
    
    [BR] Find previous envelope point before time position in the envelope object allocated with BR_EnvAlloc
    . Returns envelope point id (zero-based) on success or -1 on failure.
    """
    a=rpr_getfp('BR_EnvFindPrevious')
    f=CFUNCTYPE(c_int,c_uint64,c_double)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_double(position))
    r=f(t[0],t[1])
    return r
     
def BR_EnvFree(envelope,commit):
    """
    Python: Boolean  BR_EnvFree(BR_Envelope envelope, Boolean commit)
    
    [BR] Free envelope object allocated with BR_EnvAlloc
     and commit changes if needed. Returns true if changes were committed successfully. Note that when envelope object wasn't modified nothing will get committed even if commit = true - in that case function returns false.
    """
    a=rpr_getfp('BR_EnvFree')
    f=CFUNCTYPE(c_byte,c_uint64,c_byte)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_byte(commit))
    r=f(t[0],t[1])
    return r
     
def BR_EnvGetParentTake(envelope):
    """
    Python: MediaItem_Take  BR_EnvGetParentTake(BR_Envelope envelope)
    
    [BR] If envelope object allocated with BR_EnvAlloc
     is take envelope, returns parent media item take, otherwise NULL.
    """
    a=rpr_getfp('BR_EnvGetParentTake')
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('BR_Envelope*',envelope),)
    r=f(t[0])
    return rpr_unpackp('MediaItem_Take*',r)
     
def BR_EnvGetParentTrack(envelope):
    """
    Python: MediaItem  BR_EnvGetParentTrack(BR_Envelope envelope)
    
    [BR] Get parent track of envelope object allocated with BR_EnvAlloc
    . If take envelope, returns NULL.
    """
    a=rpr_getfp('BR_EnvGetParentTrack')
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('BR_Envelope*',envelope),)
    r=f(t[0])
    return rpr_unpackp('MediaItem*',r)
     
def BR_EnvGetPoint(envelope,Id,positionOut,valueOut,shapeOut,selectedOut,bezierOut):
    """
    Python: (Boolean retval, BR_Envelope envelope, Int id, Float positionOut, Float valueOut, Int shapeOut, Boolean selectedOut, Float bezierOut) = BR_EnvGetPoint(envelope, id, positionOut, valueOut, shapeOut, selectedOut, bezierOut)
    
    [BR] Get envelope point by id (zero-based) from the envelope object allocated with BR_EnvAlloc
    . Returns true on success.
    """
    a=rpr_getfp('BR_EnvGetPoint')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_int(Id),c_double(positionOut),c_double(valueOut),c_int(shapeOut),c_byte(selectedOut),c_double(bezierOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]))
    return (r,envelope,Id,float(t[2].value),float(t[3].value),int(t[4].value),int(t[5].value),float(t[6].value))
     
def BR_EnvGetProperties(envelope,activeOut,visibleOut,armedOut,inLaneOut,laneHeightOut,defaultShapeOut,minValueOut,maxValueOut,centerValueOut,typeOut,faderScalingOut):
    """
    Python: (BR_Envelope envelope, Boolean activeOut, Boolean visibleOut, Boolean armedOut, Boolean inLaneOut, Int laneHeightOut, Int defaultShapeOut, Float minValueOut, Float maxValueOut, Float centerValueOut, Int typeOut, Boolean faderScalingOut) = BR_EnvGetProperties(envelope, activeOut, visibleOut, armedOut, inLaneOut, laneHeightOut, defaultShapeOut, minValueOut, maxValueOut, centerValueOut, typeOut, faderScalingOut)
    
    [BR] Get envelope properties for the envelope object allocated with BR_EnvAlloc
    .
    
    
    active: true if envelope is active
    
    visible: true if envelope is visible
    
    armed: true if envelope is armed
    
    inLane: true if envelope has it's own envelope lane
    
    laneHeight: envelope lane override height. 0 for none, otherwise size in pixels
    
    defaultShape: default point shape: 0->Linear, 1->Square, 2->Slow start/end, 3->Fast start, 4->Fast end, 5->Bezier
    
    minValue: minimum envelope value
    
    maxValue: maximum envelope value
    
    type: envelope type: 0->Volume, 1->Volume (Pre-FX), 2->Pan, 3->Pan (Pre-FX), 4->Width, 5->Width (Pre-FX), 6->Mute, 7->Pitch, 8->Playrate, 9->Tempo map, 10->Parameter
    
    faderScaling: true if envelope uses fader scaling
    """
    a=rpr_getfp('BR_EnvGetProperties')
    f=CFUNCTYPE(None,c_uint64,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_byte(activeOut),c_byte(visibleOut),c_byte(armedOut),c_byte(inLaneOut),c_int(laneHeightOut),c_int(defaultShapeOut),c_double(minValueOut),c_double(maxValueOut),c_double(centerValueOut),c_int(typeOut),c_byte(faderScalingOut))
    f(t[0],byref(t[1]),byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]),byref(t[9]),byref(t[10]),byref(t[11]))
    return (envelope,int(t[1].value),int(t[2].value),int(t[3].value),int(t[4].value),int(t[5].value),int(t[6].value),float(t[7].value),float(t[8].value),float(t[9].value),int(t[10].value),int(t[11].value))
     
def BR_EnvSetPoint(envelope,Id,position,value,shape,selected,bezier):
    """
    Python: Boolean  BR_EnvSetPoint(BR_Envelope envelope, Int id, Float position, Float value, Int shape, Boolean selected, Float bezier)
    
    [BR] Set envelope point by id (zero-based) in the envelope object allocated with BR_EnvAlloc
    . To create point instead, pass id = -1. Note that if new point is inserted or existing point's time position is changed, points won't automatically get sorted. To do that, see BR_EnvSortPoints
    .
    
    Returns true on success.
    """
    a=rpr_getfp('BR_EnvSetPoint')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double,c_double,c_int,c_byte,c_double)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_int(Id),c_double(position),c_double(value),c_int(shape),c_byte(selected),c_double(bezier))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return r
     
def BR_EnvSetProperties(envelope,active,visible,armed,inLane,laneHeight,defaultShape,faderScaling):
    """
    Python: BR_EnvSetProperties(BR_Envelope envelope, Boolean active, Boolean visible, Boolean armed, Boolean inLane, Int laneHeight, Int defaultShape, Boolean faderScaling)
    
    [BR] Set envelope properties for the envelope object allocated with BR_EnvAlloc
    . For parameter description see BR_EnvGetProperties
    .
    """
    a=rpr_getfp('BR_EnvSetProperties')
    f=CFUNCTYPE(None,c_uint64,c_byte,c_byte,c_byte,c_byte,c_int,c_int,c_byte)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_byte(active),c_byte(visible),c_byte(armed),c_byte(inLane),c_int(laneHeight),c_int(defaultShape),c_byte(faderScaling))
    f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7])
     
def BR_EnvSortPoints(envelope):
    """
    Python: BR_EnvSortPoints(BR_Envelope envelope)
    
    [BR] Sort envelope points by position. The only reason to call this is if sorted points are explicitly needed after editing them with BR_EnvSetPoint
    . Note that you do not have to call this before doing BR_EnvFree
     since it does handle unsorted points too.
    """
    a=rpr_getfp('BR_EnvSortPoints')
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('BR_Envelope*',envelope),)
    f(t[0])
     
def BR_EnvValueAtPos(envelope,position):
    """
    Python: Float  BR_EnvValueAtPos(BR_Envelope envelope, Float position)
    
    [BR] Get envelope value at time position for the envelope object allocated with BR_EnvAlloc
    .
    """
    a=rpr_getfp('BR_EnvValueAtPos')
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('BR_Envelope*',envelope),c_double(position))
    r=f(t[0],t[1])
    return r
     
def BR_GetArrangeView(proj,startTimeOut,endTimeOut):
    """
    Python: (ReaProject proj, Float startTimeOut, Float endTimeOut) = BR_GetArrangeView(proj, startTimeOut, endTimeOut)
    
    [BR] Deprecated, see GetSet_ArrangeView2
     (REAPER v5.12pre4+) -- Get start and end time position of arrange view. To set arrange view instead, see BR_SetArrangeView
    .
    """
    a=rpr_getfp('BR_GetArrangeView')
    f=CFUNCTYPE(None,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(startTimeOut),c_double(endTimeOut))
    f(t[0],byref(t[1]),byref(t[2]))
    return (proj,float(t[1].value),float(t[2].value))
     
def BR_GetClosestGridDivision(position):
    """
    Python: Float  BR_GetClosestGridDivision(Float position)
    
    [BR] Get closest grid division to position. Note that this functions is different from SnapToGrid
     in two regards. SnapToGrid() needs snap enabled to work and this one works always. Secondly, grid divisions are different from grid lines because some grid lines may be hidden due to zoom level - this function ignores grid line visibility and always searches for the closest grid division at given position. For more grid division functions, see BR_GetNextGridDivision
     and BR_GetPrevGridDivision
    .
    """
    a=rpr_getfp('BR_GetClosestGridDivision')
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(position),)
    r=f(t[0])
    return r
     
def BR_GetCurrentTheme(themePathOut,themePathOut_sz,themeNameOut,themeNameOut_sz):
    """
    Python: (String themePathOut, Int themePathOut_sz, String themeNameOut, Int themeNameOut_sz) = BR_GetCurrentTheme(themePathOut, themePathOut_sz, themeNameOut, themeNameOut_sz)
    
    [BR] Get current theme information. themePathOut is set to full theme path and themeNameOut is set to theme name excluding any path info and extension
    """
    a=rpr_getfp('BR_GetCurrentTheme')
    f=CFUNCTYPE(None,c_char_p,c_int,c_char_p,c_int)(a)
    t=(rpr_packs(themePathOut),c_int(themePathOut_sz),rpr_packs(themeNameOut),c_int(themeNameOut_sz))
    f(t[0],t[1],t[2],t[3])
    return (rpr_unpacks(t[0]),themePathOut_sz,rpr_unpacks(t[2]),themeNameOut_sz)
     
def BR_GetMediaItemByGUID(proj,guidStringIn):
    """
    Python: MediaItem  BR_GetMediaItemByGUID(ReaProject proj, String guidStringIn)
    
    [BR] Get media item from GUID string. Note that the GUID must be enclosed in braces {}. To get item's GUID as a string, see BR_GetMediaItemGUID
    .
    """
    a=rpr_getfp('BR_GetMediaItemByGUID')
    f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(guidStringIn))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem*',r)
     
def BR_GetMediaItemGUID(item,guidStringOut,guidStringOut_sz):
    """
    Python: (MediaItem item, String guidStringOut, Int guidStringOut_sz) = BR_GetMediaItemGUID(item, guidStringOut, guidStringOut_sz)
    
    [BR] Get media item GUID as a string (guidStringOut_sz should be at least 64). To get media item back from GUID string, see BR_GetMediaItemByGUID
    .
    """
    a=rpr_getfp('BR_GetMediaItemGUID')
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packs(guidStringOut),c_int(guidStringOut_sz))
    f(t[0],t[1],t[2])
    return (item,rpr_unpacks(t[1]),guidStringOut_sz)
     
def BR_GetMediaItemImageResource(item,imageOut,imageOut_sz,imageFlagsOut):
    """
    Python: (Boolean retval, MediaItem item, String imageOut, Int imageOut_sz, Int imageFlagsOut) = BR_GetMediaItemImageResource(item, imageOut, imageOut_sz, imageFlagsOut)
    
    [BR] Get currently loaded image resource and it's flags for a given item. Returns false if there is no image resource set. To set image resource, see BR_SetMediaItemImageResource
    .
    """
    a=rpr_getfp('BR_GetMediaItemImageResource')
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packs(imageOut),c_int(imageOut_sz),c_int(imageFlagsOut))
    r=f(t[0],t[1],t[2],byref(t[3]))
    return (r,item,rpr_unpacks(t[1]),imageOut_sz,int(t[3].value))
     
def BR_GetMediaItemTakeGUID(take,guidStringOut,guidStringOut_sz):
    """
    Python: (MediaItem_Take take, String guidStringOut, Int guidStringOut_sz) = BR_GetMediaItemTakeGUID(take, guidStringOut, guidStringOut_sz)
    
    [BR] Get media item take GUID as a string (guidStringOut_sz should be at least 64). To get take from GUID string, see SNM_GetMediaItemTakeByGUID
    .
    """
    a=rpr_getfp('BR_GetMediaItemTakeGUID')
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packs(guidStringOut),c_int(guidStringOut_sz))
    f(t[0],t[1],t[2])
    return (take,rpr_unpacks(t[1]),guidStringOut_sz)
     
def BR_GetMediaSourceProperties(take,sectionOut,startOut,lengthOut,fadeOut,reverseOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Boolean sectionOut, Float startOut, Float lengthOut, Float fadeOut, Boolean reverseOut) = BR_GetMediaSourceProperties(take, sectionOut, startOut, lengthOut, fadeOut, reverseOut)
    
    [BR] Get take media source properties as they appear in Item properties
    . Returns false if take can't have them (MIDI items etc.).
    
    To set source properties, see BR_SetMediaSourceProperties
    .
    """
    a=rpr_getfp('BR_GetMediaSourceProperties')
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(sectionOut),c_double(startOut),c_double(lengthOut),c_double(fadeOut),c_byte(reverseOut))
    r=f(t[0],byref(t[1]),byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]))
    return (r,take,int(t[1].value),float(t[2].value),float(t[3].value),float(t[4].value),int(t[5].value))
     
def BR_GetMediaTrackByGUID(proj,guidStringIn):
    """
    Python: MediaTrack  BR_GetMediaTrackByGUID(ReaProject proj, String guidStringIn)
    
    [BR] Get media track from GUID string. Note that the GUID must be enclosed in braces {}. To get track's GUID as a string, see BR_GetMediaTrackGUID
    .
    """
    a=rpr_getfp('BR_GetMediaTrackByGUID')
    f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(guidStringIn))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaTrack*',r)
     
def BR_GetMediaTrackFreezeCount(track):
    """
    Python: Int  BR_GetMediaTrackFreezeCount(MediaTrack track)
    
    [BR] Get media track freeze count (if track isn't frozen at all, returns 0).
    """
    a=rpr_getfp('BR_GetMediaTrackFreezeCount')
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def BR_GetMediaTrackGUID(track,guidStringOut,guidStringOut_sz):
    """
    Python: (MediaTrack track, String guidStringOut, Int guidStringOut_sz) = BR_GetMediaTrackGUID(track, guidStringOut, guidStringOut_sz)
    
    [BR] Get media track GUID as a string (guidStringOut_sz should be at least 64). To get media track back from GUID string, see BR_GetMediaTrackByGUID
    .
    """
    a=rpr_getfp('BR_GetMediaTrackGUID')
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packs(guidStringOut),c_int(guidStringOut_sz))
    f(t[0],t[1],t[2])
    return (track,rpr_unpacks(t[1]),guidStringOut_sz)
     
def BR_GetMediaTrackLayouts(track,mcpLayoutNameOut,mcpLayoutNameOut_sz,tcpLayoutNameOut,tcpLayoutNameOut_sz):
    """
    Python: (MediaTrack track, String mcpLayoutNameOut, Int mcpLayoutNameOut_sz, String tcpLayoutNameOut, Int tcpLayoutNameOut_sz) = BR_GetMediaTrackLayouts(track, mcpLayoutNameOut, mcpLayoutNameOut_sz, tcpLayoutNameOut, tcpLayoutNameOut_sz)
    
    [BR] Deprecated, see GetSetMediaTrackInfo
     (REAPER v5.02+). Get media track layouts for MCP and TCP. Empty string ("") means that layout is set to the default layout. To set media track layouts, see BR_SetMediaTrackLayouts
    .
    """
    a=rpr_getfp('BR_GetMediaTrackLayouts')
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packs(mcpLayoutNameOut),c_int(mcpLayoutNameOut_sz),rpr_packs(tcpLayoutNameOut),c_int(tcpLayoutNameOut_sz))
    f(t[0],t[1],t[2],t[3],t[4])
    return (track,rpr_unpacks(t[1]),mcpLayoutNameOut_sz,rpr_unpacks(t[3]),tcpLayoutNameOut_sz)
     
def BR_GetMediaTrackSendInfo_Envelope(track,category,sendidx,envelopeType):
    """
    Python: TrackEnvelope  BR_GetMediaTrackSendInfo_Envelope(MediaTrack track, Int category, Int sendidx, Int envelopeType)
    
    [BR] Get track envelope for send/receive/hardware output.
    
    
    category is <0 for receives, 0=sends, >0 for hardware outputs
    
    sendidx is zero-based (see GetTrackNumSends
     to count track sends/receives/hardware outputs)
    
    envelopeType determines which envelope is returned (0=volume, 1=pan, 2=mute)
    
    
    Note: To get or set other send attributes, see BR_GetSetTrackSendInfo
     and BR_GetMediaTrackSendInfo_Track
    .
    """
    a=rpr_getfp('BR_GetMediaTrackSendInfo_Envelope')
    f=CFUNCTYPE(c_uint64,c_uint64,c_int,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(category),c_int(sendidx),c_int(envelopeType))
    r=f(t[0],t[1],t[2],t[3])
    return rpr_unpackp('TrackEnvelope*',r)
     
def BR_GetMediaTrackSendInfo_Track(track,category,sendidx,trackType):
    """
    Python: MediaTrack  BR_GetMediaTrackSendInfo_Track(MediaTrack track, Int category, Int sendidx, Int trackType)
    
    [BR] Get source or destination media track for send/receive.
    
    
    category is <0 for receives, 0=sends
    
    sendidx is zero-based (see GetTrackNumSends
     to count track sends/receives)
    
    trackType determines which track is returned (0=source track, 1=destination track)
    
    
    Note: To get or set other send attributes, see BR_GetSetTrackSendInfo
     and BR_GetMediaTrackSendInfo_Envelope
    .
    """
    a=rpr_getfp('BR_GetMediaTrackSendInfo_Track')
    f=CFUNCTYPE(c_uint64,c_uint64,c_int,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(category),c_int(sendidx),c_int(trackType))
    r=f(t[0],t[1],t[2],t[3])
    return rpr_unpackp('MediaTrack*',r)
     
def BR_GetMidiSourceLenPPQ(take):
    """
    Python: Float  BR_GetMidiSourceLenPPQ(MediaItem_Take take)
    
    [BR] Get MIDI take source length in PPQ. In case the take isn't MIDI, return value will be -1.
    """
    a=rpr_getfp('BR_GetMidiSourceLenPPQ')
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def BR_GetMidiTakePoolGUID(take,guidStringOut,guidStringOut_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, String guidStringOut, Int guidStringOut_sz) = BR_GetMidiTakePoolGUID(take, guidStringOut, guidStringOut_sz)
    
    [BR] Get MIDI take pool GUID as a string (guidStringOut_sz should be at least 64). Returns true if take is pooled.
    """
    a=rpr_getfp('BR_GetMidiTakePoolGUID')
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packs(guidStringOut),c_int(guidStringOut_sz))
    r=f(t[0],t[1],t[2])
    return (r,take,rpr_unpacks(t[1]),guidStringOut_sz)
     
def BR_GetMidiTakeTempoInfo(take,ignoreProjTempoOut,bpmOut,numOut,denOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Boolean ignoreProjTempoOut, Float bpmOut, Int numOut, Int denOut) = BR_GetMidiTakeTempoInfo(take, ignoreProjTempoOut, bpmOut, numOut, denOut)
    
    [BR] Get "ignore project tempo" information for MIDI take. Returns true if take can ignore project tempo (no matter if it's actually ignored), otherwise false.
    """
    a=rpr_getfp('BR_GetMidiTakeTempoInfo')
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(ignoreProjTempoOut),c_double(bpmOut),c_int(numOut),c_int(denOut))
    r=f(t[0],byref(t[1]),byref(t[2]),byref(t[3]),byref(t[4]))
    return (r,take,int(t[1].value),float(t[2].value),int(t[3].value),int(t[4].value))
     
def BR_GetMouseCursorContext(windowOut,windowOut_sz,segmentOut,segmentOut_sz,detailsOut,detailsOut_sz):
    """
    Python: (String windowOut, Int windowOut_sz, String segmentOut, Int segmentOut_sz, String detailsOut, Int detailsOut_sz) = BR_GetMouseCursorContext(windowOut, windowOut_sz, segmentOut, segmentOut_sz, detailsOut, detailsOut_sz)
    
    [BR] Get mouse cursor context. Each parameter returns information in a form of string as specified in the table below.
    
    
    To get more info on stuff that was found under mouse cursor see BR_GetMouseCursorContext_Envelope
    , BR_GetMouseCursorContext_Item
    , BR_GetMouseCursorContext_MIDI
    , BR_GetMouseCursorContext_Position
    , BR_GetMouseCursorContext_Take
    , BR_GetMouseCursorContext_Track 
    
    Window Segment Details  unknown       ""          ""                                                             ruler         region_lane   ""                                                              marker_lane   ""                                                              tempo_lane    ""                                                              timeline      ""                                                             transport     ""          ""                                                             tcp           track         ""                                                              envelope      ""                                                              empty         ""                                                             mcp           track         ""                                                              empty         ""                                                             arrange       track         empty,item, item_stretch_marker,env_point, env_segment    envelope      empty, env_point, env_segment                                     empty         ""                                                             midi_editor   unknown       ""                                                              ruler         ""                                                              piano         ""                                                              notes         ""                                                              cc_lane       cc_selector, cc_lane
    """
    a=rpr_getfp('BR_GetMouseCursorContext')
    f=CFUNCTYPE(None,c_char_p,c_int,c_char_p,c_int,c_char_p,c_int)(a)
    t=(rpr_packs(windowOut),c_int(windowOut_sz),rpr_packs(segmentOut),c_int(segmentOut_sz),rpr_packs(detailsOut),c_int(detailsOut_sz))
    f(t[0],t[1],t[2],t[3],t[4],t[5])
    return (rpr_unpacks(t[0]),windowOut_sz,rpr_unpacks(t[2]),segmentOut_sz,rpr_unpacks(t[4]),detailsOut_sz)
     
def BR_GetMouseCursorContext_Envelope(takeEnvelopeOut):
    """
    Python: (TrackEnvelope retval, Boolean takeEnvelopeOut) = BR_GetMouseCursorContext_Envelope(takeEnvelopeOut)
    
    [BR] Returns envelope that was captured with the last call to BR_GetMouseCursorContext
    . In case the envelope belongs to take, takeEnvelope will be true.
    """
    a=rpr_getfp('BR_GetMouseCursorContext_Envelope')
    f=CFUNCTYPE(c_uint64,c_void_p)(a)
    t=(c_byte(takeEnvelopeOut),)
    r=f(byref(t[0]))
    return (rpr_unpackp('TrackEnvelope*',r),int(t[0].value))
     
def BR_GetMouseCursorContext_Item():
    """
    Python: MediaItem  BR_GetMouseCursorContext_Item()
    
    [BR] Returns item under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
    . Note that the function will return item even if mouse cursor is over some other track lane element like stretch marker or envelope. This enables for easier identification of items when you want to ignore elements within the item.
    """
    a=rpr_getfp('BR_GetMouseCursorContext_Item')
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('MediaItem*',r)
     
def BR_GetMouseCursorContext_MIDI(inlineEditorOut,noteRowOut,ccLaneOut,ccLaneValOut,ccLaneIdOut):
    """
    Python: (void retval, Boolean inlineEditorOut, Int noteRowOut, Int ccLaneOut, Int ccLaneValOut, Int ccLaneIdOut) = BR_GetMouseCursorContext_MIDI(inlineEditorOut, noteRowOut, ccLaneOut, ccLaneValOut, ccLaneIdOut)
    
    [BR] Returns midi editor under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
    .
    
    
    inlineEditor: if mouse was captured in inline MIDI editor, this will be true (consequentially, returned MIDI editor will be NULL)
    
    noteRow: note row or piano key under mouse cursor (0-127)
    
    ccLane: CC lane under mouse cursor (CC0-127=CC, 0x100|(0-31)=14-bit CC, 0x200=velocity, 0x201=pitch, 0x202=program, 0x203=channel pressure, 0x204=bank/program select, 0x205=text, 0x206=sysex, 0x207=off velocity)
    
    ccLaneVal: value in CC lane under mouse cursor (0-127 or 0-16383)
    
    ccLaneId: lane position, counting from the top (0 based)
    
    
    Note: due to API limitations, if mouse is over inline MIDI editor with some note rows hidden, noteRow will be -1
    """
    a=rpr_getfp('BR_GetMouseCursorContext_MIDI')
    f=CFUNCTYPE(c_uint64,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(c_byte(inlineEditorOut),c_int(noteRowOut),c_int(ccLaneOut),c_int(ccLaneValOut),c_int(ccLaneIdOut))
    r=f(byref(t[0]),byref(t[1]),byref(t[2]),byref(t[3]),byref(t[4]))
    return (rpr_unpackp('void*',r),int(t[0].value),int(t[1].value),int(t[2].value),int(t[3].value),int(t[4].value))
     
def BR_GetMouseCursorContext_Position():
    """
    Python: Float  BR_GetMouseCursorContext_Position()
    
    [BR] Returns project time position in arrange/ruler/midi editor that was captured with the last call to BR_GetMouseCursorContext
    .
    """
    a=rpr_getfp('BR_GetMouseCursorContext_Position')
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def BR_GetMouseCursorContext_StretchMarker():
    """
    Python: Int  BR_GetMouseCursorContext_StretchMarker()
    
    [BR] Returns id of a stretch marker under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
    .
    """
    a=rpr_getfp('BR_GetMouseCursorContext_StretchMarker')
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def BR_GetMouseCursorContext_Take():
    """
    Python: MediaItem_Take  BR_GetMouseCursorContext_Take()
    
    [BR] Returns take under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
    .
    """
    a=rpr_getfp('BR_GetMouseCursorContext_Take')
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('MediaItem_Take*',r)
     
def BR_GetMouseCursorContext_Track():
    """
    Python: MediaTrack  BR_GetMouseCursorContext_Track()
    
    [BR] Returns track under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
    .
    """
    a=rpr_getfp('BR_GetMouseCursorContext_Track')
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('MediaTrack*',r)
     
def BR_GetNextGridDivision(position):
    """
    Python: Float  BR_GetNextGridDivision(Float position)
    
    [BR] Get next grid division after the time position. For more grid divisions function, see BR_GetClosestGridDivision
     and BR_GetPrevGridDivision
    .
    """
    a=rpr_getfp('BR_GetNextGridDivision')
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(position),)
    r=f(t[0])
    return r
     
def BR_GetPrevGridDivision(position):
    """
    Python: Float  BR_GetPrevGridDivision(Float position)
    
    [BR] Get previous grid division before the time position. For more grid division functions, see BR_GetClosestGridDivision
     and BR_GetNextGridDivision
    .
    """
    a=rpr_getfp('BR_GetPrevGridDivision')
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(position),)
    r=f(t[0])
    return r
     
def BR_GetSetTrackSendInfo(track,category,sendidx,parmname,setNewValue,newValue):
    """
    Python: Float  BR_GetSetTrackSendInfo(MediaTrack track, Int category, Int sendidx, String parmname, Boolean setNewValue, Float newValue)
    
    [BR] Get or set send attributes.
    
    
    category is <0 for receives, 0=sends, >0 for hardware outputs
    
    sendidx is zero-based (see GetTrackNumSends
     to count track sends/receives/hardware outputs)
    
    To set attribute, pass setNewValue as true
    
    
    List of possible parameters:
    
    B_MUTE : send mute state (1.0 if muted, otherwise 0.0)
    
    B_PHASE : send phase state (1.0 if phase is inverted, otherwise 0.0)
    
    B_MONO : send mono state (1.0 if send is set to mono, otherwise 0.0)
    
    D_VOL : send volume (1.0=+0dB etc...)
    
    D_PAN : send pan (-1.0=100%L, 0=center, 1.0=100%R)
    
    D_PANLAW : send pan law (1.0=+0.0db, 0.5=-6dB, -1.0=project default etc...)
    
    I_SENDMODE : send mode (0=post-fader, 1=pre-fx, 2=post-fx(deprecated), 3=post-fx)
    
    I_SRCCHAN : audio source starting channel index or -1 if audio send is disabled (&1024=mono...note that in that case, when reading index, you should do (index XOR 1024) to get starting channel index)
    
    I_DSTCHAN : audio destination starting channel index (&1024=mono (and in case of hardware output &512=rearoute)...note that in that case, when reading index, you should do (index XOR (1024 OR 512)) to get starting channel index)
    
    I_MIDI_SRCCHAN : source MIDI channel, -1 if MIDI send is disabled (0=all, 1-16)
    
    I_MIDI_DSTCHAN : destination MIDI channel, -1 if MIDI send is disabled (0=original, 1-16)
    
    I_MIDI_SRCBUS : source MIDI bus, -1 if MIDI send is disabled (0=all, otherwise bus index)
    
    I_MIDI_DSTBUS : receive MIDI bus, -1 if MIDI send is disabled (0=all, otherwise bus index)
    
    I_MIDI_LINK_VOLPAN : link volume/pan controls to MIDI
    
    
    Note: To get or set other send attributes, see BR_GetMediaTrackSendInfo_Envelope
     and BR_GetMediaTrackSendInfo_Track
    .
    """
    a=rpr_getfp('BR_GetSetTrackSendInfo')
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int,c_char_p,c_byte,c_double)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(category),c_int(sendidx),rpr_packsc(parmname),c_byte(setNewValue),c_double(newValue))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def BR_GetTakeFXCount(take):
    """
    Python: Int  BR_GetTakeFXCount(MediaItem_Take take)
    
    [BR] Returns FX count for supplied take
    """
    a=rpr_getfp('BR_GetTakeFXCount')
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def BR_IsMidiOpenInInlineEditor(take):
    """
    Python: Boolean  BR_IsMidiOpenInInlineEditor(MediaItem_Take take)
    
    [SWS] Check if take has MIDI inline editor open and returns true or false.
    """
    a=rpr_getfp('BR_IsMidiOpenInInlineEditor')
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def BR_IsTakeMidi(take,inProjectMidiOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Boolean inProjectMidiOut) = BR_IsTakeMidi(take, inProjectMidiOut)
    
    [BR] Check if take is MIDI take, in case MIDI take is in-project MIDI source data, inProjectMidiOut will be true, otherwise false.
    """
    a=rpr_getfp('BR_IsTakeMidi')
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(inProjectMidiOut))
    r=f(t[0],byref(t[1]))
    return (r,take,int(t[1].value))
     
def BR_ItemAtMouseCursor(positionOut):
    """
    Python: (MediaItem retval, Float positionOut) = BR_ItemAtMouseCursor(positionOut)
    
    [BR] Get media item under mouse cursor. Position is mouse cursor position in arrange.
    """
    a=rpr_getfp('BR_ItemAtMouseCursor')
    f=CFUNCTYPE(c_uint64,c_void_p)(a)
    t=(c_double(positionOut),)
    r=f(byref(t[0]))
    return (rpr_unpackp('MediaItem*',r),float(t[0].value))
     
def BR_MIDI_CCLaneRemove(midiEditor,laneId):
    """
    Python: Boolean  BR_MIDI_CCLaneRemove(HWND midiEditor, Int laneId)
    
    [BR] Remove CC lane in midi editor. Returns true on success
    """
    a=rpr_getfp('BR_MIDI_CCLaneRemove')
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('HWND',midiEditor),c_int(laneId))
    r=f(t[0],t[1])
    return r
     
def BR_MIDI_CCLaneReplace(midiEditor,laneId,newCC):
    """
    Python: Boolean  BR_MIDI_CCLaneReplace(HWND midiEditor, Int laneId, Int newCC)
    
    [BR] Replace CC lane in midi editor. Returns true on success.
    
    Valid CC lanes: CC0-127=CC, 0x100|(0-31)=14-bit CC, 0x200=velocity, 0x201=pitch, 0x202=program, 0x203=channel pressure, 0x204=bank/program select, 0x205=text, 0x206=sysex, 0x207
    """
    a=rpr_getfp('BR_MIDI_CCLaneReplace')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('HWND',midiEditor),c_int(laneId),c_int(newCC))
    r=f(t[0],t[1],t[2])
    return r
     
def BR_PositionAtMouseCursor(checkRuler):
    """
    Python: Float  BR_PositionAtMouseCursor(Boolean checkRuler)
    
    [BR] Get position at mouse cursor. To check ruler along with arrange, pass checkRuler=true. Returns -1 if cursor is not over arrange/ruler.
    """
    a=rpr_getfp('BR_PositionAtMouseCursor')
    f=CFUNCTYPE(c_double,c_byte)(a)
    t=(c_byte(checkRuler),)
    r=f(t[0])
    return r
     
def BR_SetArrangeView(proj,startTime,endTime):
    """
    Python: BR_SetArrangeView(ReaProject proj, Float startTime, Float endTime)
    
    [BR] Deprecated, see GetSet_ArrangeView2
     (REAPER v5.12pre4+) -- Set start and end time position of arrange view. To get arrange view instead, see BR_GetArrangeView
    .
    """
    a=rpr_getfp('BR_SetArrangeView')
    f=CFUNCTYPE(None,c_uint64,c_double,c_double)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(startTime),c_double(endTime))
    f(t[0],t[1],t[2])
     
def BR_SetItemEdges(item,startTime,endTime):
    """
    Python: Boolean  BR_SetItemEdges(MediaItem item, Float startTime, Float endTime)
    
    [BR] Set item start and end edges' position - returns true in case of any changes
    """
    a=rpr_getfp('BR_SetItemEdges')
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_double)(a)
    t=(rpr_packp('MediaItem*',item),c_double(startTime),c_double(endTime))
    r=f(t[0],t[1],t[2])
    return r
     
def BR_SetMediaItemImageResource(item,imageIn,imageFlags):
    """
    Python: BR_SetMediaItemImageResource(MediaItem item, String imageIn, Int imageFlags)
    
    [BR] Set image resource and it's flags for a given item. To clear current image resource, pass imageIn as . To get image resource, see BR_GetMediaItemImageResource
    .
    """
    a=rpr_getfp('BR_SetMediaItemImageResource')
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packsc(imageIn),c_int(imageFlags))
    f(t[0],t[1],t[2])
     
def BR_SetMediaSourceProperties(take,section,start,length,fade,reverse):
    """
    Python: Boolean  BR_SetMediaSourceProperties(MediaItem_Take take, Boolean section, Float start, Float length, Float fade, Boolean reverse)
    
    [BR] Set take media source properties. Returns false if take can't have them (MIDI items etc.). Section parameters have to be valid only when passing section=true.
    
    To get source properties, see BR_GetMediaSourceProperties
    .
    """
    a=rpr_getfp('BR_SetMediaSourceProperties')
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_double,c_double,c_double,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(section),c_double(start),c_double(length),c_double(fade),c_byte(reverse))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def BR_SetMediaTrackLayouts(track,mcpLayoutNameIn,tcpLayoutNameIn):
    """
    Python: Boolean  BR_SetMediaTrackLayouts(MediaTrack track, String mcpLayoutNameIn, String tcpLayoutNameIn)
    
    [BR] Deprecated, see GetSetMediaTrackInfo
     (REAPER v5.02+). Set media track layouts for MCP and TCP. To set default layout, pass empty string ("") as layout name. In case layouts were successfully set, returns true (if layouts are already set to supplied layout names, it will return false since no changes were made).
    
    To get media track layouts, see BR_GetMediaTrackLayouts
    .
    """
    a=rpr_getfp('BR_SetMediaTrackLayouts')
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packsc(mcpLayoutNameIn),rpr_packsc(tcpLayoutNameIn))
    r=f(t[0],t[1],t[2])
    return r
     
def BR_SetMidiTakeTempoInfo(take,ignoreProjTempo,bpm,num,den):
    """
    Python: Boolean  BR_SetMidiTakeTempoInfo(MediaItem_Take take, Boolean ignoreProjTempo, Float bpm, Int num, Int den)
    
    [BR] Set "ignore project tempo" information for MIDI take. Returns true in case the take was successfully updated.
    """
    a=rpr_getfp('BR_SetMidiTakeTempoInfo')
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_double,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(ignoreProjTempo),c_double(bpm),c_int(num),c_int(den))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def BR_SetTakeSourceFromFile(take,filenameIn,inProjectData):
    """
    Python: Boolean  BR_SetTakeSourceFromFile(MediaItem_Take take, String filenameIn, Boolean inProjectData)
    
    [BR] Set new take source from file. To import MIDI file as in-project source data pass inProjectData=true. Returns false if failed.
    
    Any take source properties from the previous source will be lost - to preserve them, see BR_SetTakeSourceFromFile2
    .
    
    Note: To set source from existing take, see SNM_GetSetSourceState2
    .
    """
    a=rpr_getfp('BR_SetTakeSourceFromFile')
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packsc(filenameIn),c_byte(inProjectData))
    r=f(t[0],t[1],t[2])
    return r
     
def BR_SetTakeSourceFromFile2(take,filenameIn,inProjectData,keepSourceProperties):
    """
    Python: Boolean  BR_SetTakeSourceFromFile2(MediaItem_Take take, String filenameIn, Boolean inProjectData, Boolean keepSourceProperties)
    
    [BR] Differs from BR_SetTakeSourceFromFile
     only that it can also preserve existing take media source properties.
    """
    a=rpr_getfp('BR_SetTakeSourceFromFile2')
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_byte,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packsc(filenameIn),c_byte(inProjectData),c_byte(keepSourceProperties))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def BR_TakeAtMouseCursor(positionOut):
    """
    Python: (MediaItem_Take retval, Float positionOut) = BR_TakeAtMouseCursor(positionOut)
    
    [BR] Get take under mouse cursor. Position is mouse cursor position in arrange.
    """
    a=rpr_getfp('BR_TakeAtMouseCursor')
    f=CFUNCTYPE(c_uint64,c_void_p)(a)
    t=(c_double(positionOut),)
    r=f(byref(t[0]))
    return (rpr_unpackp('MediaItem_Take*',r),float(t[0].value))
     
def BR_TrackAtMouseCursor(contextOut,positionOut):
    """
    Python: (MediaTrack retval, Int contextOut, Float positionOut) = BR_TrackAtMouseCursor(contextOut, positionOut)
    
    [BR] Get track under mouse cursor.
    
    Context signifies where the track was found: 0 = TCP, 1 = MCP, 2 = Arrange.
    
    Position will hold mouse cursor position in arrange if applicable.
    """
    a=rpr_getfp('BR_TrackAtMouseCursor')
    f=CFUNCTYPE(c_uint64,c_void_p,c_void_p)(a)
    t=(c_int(contextOut),c_double(positionOut))
    r=f(byref(t[0]),byref(t[1]))
    return (rpr_unpackp('MediaTrack*',r),int(t[0].value),float(t[1].value))
     
def BR_TrackFX_GetFXModuleName(track,fx,nameOut,nameOutSz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, String  nameOut, Int  nameOutSz) = BR_TrackFX_GetFXModuleName(track, fx,  nameOut,  nameOutSz)
    
    [BR] Get the exact name (like effect.dll, effect.vst3, etc...) of an FX.
    """
    a=rpr_getfp('BR_TrackFX_GetFXModuleName')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),rpr_packs(nameOut),c_int(nameOutSz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,fx,rpr_unpacks(t[2]),nameOutSz)
     
def BR_Win32_GetPrivateProfileString(sectionName,keyName,defaultString,filePath,stringOut,stringOut_sz):
    """
    Python: (Int retval, String sectionName, String keyName, String defaultString, String filePath, String stringOut, Int stringOut_sz) = BR_Win32_GetPrivateProfileString(sectionName, keyName, defaultString, filePath, stringOut, stringOut_sz)
    
    [BR] Equivalent to win32 API GetPrivateProfileString(). For example, you can use this to get values from REAPER.ini
    """
    a=rpr_getfp('BR_Win32_GetPrivateProfileString')
    f=CFUNCTYPE(c_int,c_char_p,c_char_p,c_char_p,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(sectionName),rpr_packsc(keyName),rpr_packsc(defaultString),rpr_packsc(filePath),rpr_packs(stringOut),c_int(stringOut_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return (r,sectionName,keyName,defaultString,filePath,rpr_unpacks(t[4]),stringOut_sz)
     
def BR_Win32_ShellExecute(operation,file,parameters,directory,showFlags):
    """
    Python: Int  BR_Win32_ShellExecute(String operation, String file, String parameters, String directory, Int showFlags)
    
    [BR] Equivalent to win32 API ShellExecute() with HWND set to main window
    """
    a=rpr_getfp('BR_Win32_ShellExecute')
    f=CFUNCTYPE(c_int,c_char_p,c_char_p,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(operation),rpr_packsc(file),rpr_packsc(parameters),rpr_packsc(directory),c_int(showFlags))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def BR_Win32_WritePrivateProfileString(sectionName,keyName,value,filePath):
    """
    Python: Boolean  BR_Win32_WritePrivateProfileString(String sectionName, String keyName, String value, String filePath)
    
    [BR] Equivalent to win32 API WritePrivateProfileString(). For example, you can use this to write to REAPER.ini
    """
    a=rpr_getfp('BR_Win32_WritePrivateProfileString')
    f=CFUNCTYPE(c_byte,c_char_p,c_char_p,c_char_p,c_char_p)(a)
    t=(rpr_packsc(sectionName),rpr_packsc(keyName),rpr_packsc(value),rpr_packsc(filePath))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def CF_GetClipboard(buf,buf_sz):
    """
    Python: (String buf, Int buf_sz) = CF_GetClipboard(buf, buf_sz)
    
    Read the contents of the system clipboard (limited to 1023 characters in Lua).
    """
    a=rpr_getfp('CF_GetClipboard')
    f=CFUNCTYPE(None,c_char_p,c_int)(a)
    t=(rpr_packs(buf),c_int(buf_sz))
    f(t[0],t[1])
    return (rpr_unpacks(t[0]),buf_sz)
     
def CF_GetClipboardBig(output):
    """
    Python: String  CF_GetClipboardBig(WDL_FastString output)
    
    Read the contents of the system clipboard. See SNM_CreateFastString
     and SNM_DeleteFastString
    .
    """
    a=rpr_getfp('CF_GetClipboardBig')
    f=CFUNCTYPE(c_char_p,c_uint64)(a)
    t=(rpr_packp('WDL_FastString*',output),)
    r=f(t[0])
    return str(r.decode())
     
def CF_SetClipboard(Str):
    """
    Python: CF_SetClipboard(String str)
    
    Write the given string into the system clipboard.
    """
    a=rpr_getfp('CF_SetClipboard')
    f=CFUNCTYPE(None,c_char_p)(a)
    t=(rpr_packsc(Str),)
    f(t[0])
     
def FNG_AddMidiNote(midiTake):
    """
    Python: RprMidiNote  FNG_AddMidiNote(RprMidiTake midiTake)
    
    [FNG] Add MIDI note to MIDI take
    """
    a=rpr_getfp('FNG_AddMidiNote')
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('RprMidiTake*',midiTake),)
    r=f(t[0])
    return rpr_unpackp('RprMidiNote*',r)
     
def FNG_AllocMidiTake(take):
    """
    Python: RprMidiTake  FNG_AllocMidiTake(MediaItem_Take take)
    
    [FNG] Allocate a RprMidiTake from a take pointer. Returns a NULL pointer if the take is not an in-project MIDI take
    """
    a=rpr_getfp('FNG_AllocMidiTake')
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return rpr_unpackp('RprMidiTake*',r)
     
def FNG_CountMidiNotes(midiTake):
    """
    Python: Int  FNG_CountMidiNotes(RprMidiTake midiTake)
    
    [FNG] Count of how many MIDI notes are in the MIDI take
    """
    a=rpr_getfp('FNG_CountMidiNotes')
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('RprMidiTake*',midiTake),)
    r=f(t[0])
    return r
     
def FNG_FreeMidiTake(midiTake):
    """
    Python: FNG_FreeMidiTake(RprMidiTake midiTake)
    
    [FNG] Commit changes to MIDI take and free allocated memory
    """
    a=rpr_getfp('FNG_FreeMidiTake')
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('RprMidiTake*',midiTake),)
    f(t[0])
     
def FNG_GetMidiNote(midiTake,index):
    """
    Python: RprMidiNote  FNG_GetMidiNote(RprMidiTake midiTake, Int index)
    
    [FNG] Get a MIDI note from a MIDI take at specified index
    """
    a=rpr_getfp('FNG_GetMidiNote')
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('RprMidiTake*',midiTake),c_int(index))
    r=f(t[0],t[1])
    return rpr_unpackp('RprMidiNote*',r)
     
def FNG_GetMidiNoteIntProperty(midiNote,Property):
    """
    Python: Int  FNG_GetMidiNoteIntProperty(RprMidiNote midiNote, String property)
    
    [FNG] Get MIDI note property
    """
    a=rpr_getfp('FNG_GetMidiNoteIntProperty')
    f=CFUNCTYPE(c_int,c_uint64,c_char_p)(a)
    t=(rpr_packp('RprMidiNote*',midiNote),rpr_packsc(Property))
    r=f(t[0],t[1])
    return r
     
def FNG_SetMidiNoteIntProperty(midiNote,Property,value):
    """
    Python: FNG_SetMidiNoteIntProperty(RprMidiNote midiNote, String property, Int value)
    
    [FNG] Set MIDI note property
    """
    a=rpr_getfp('FNG_SetMidiNoteIntProperty')
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('RprMidiNote*',midiNote),rpr_packsc(Property),c_int(value))
    f(t[0],t[1],t[2])
     
def NF_AnalyzeTakeLoudness(take,analyzeTruePeak,lufsIntegratedOut,rangeOut,truePeakOut,truePeakPosOut,shortTermMaxOut,momentaryMaxOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Boolean analyzeTruePeak, Float lufsIntegratedOut, Float rangeOut, Float  truePeakOut, Float truePeakPosOut, Float shortTermMaxOut, Float momentaryMaxOut) = NF_AnalyzeTakeLoudness(take, analyzeTruePeak, lufsIntegratedOut, rangeOut,  truePeakOut, truePeakPosOut, shortTermMaxOut, momentaryMaxOut)
    
    Full loudness analysis. retval: returns true on successful analysis, false on MIDI take or when analysis failed for some reason. analyzeTruePeak=true: Also do true peak analysis. Returns true peak value and true peak position which can be jumped to with SetEditCurPos(). Considerably slower than without true peak analysis (since it uses oversampling). Note: Short term uses a time window of 3 sec. for calculation. So for items shorter than this shortTermMaxOut can't be calculated. Momentary uses a time window of 0.4 sec.
    """
    a=rpr_getfp('NF_AnalyzeTakeLoudness')
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(analyzeTruePeak),c_double(lufsIntegratedOut),c_double(rangeOut),c_double(truePeakOut),c_double(truePeakPosOut),c_double(shortTermMaxOut),c_double(momentaryMaxOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]))
    return (r,take,analyzeTruePeak,float(t[2].value),float(t[3].value),float(t[4].value),float(t[5].value),float(t[6].value),float(t[7].value))
     
def NF_AnalyzeTakeLoudness2(take,analyzeTruePeak,lufsIntegratedOut,rangeOut,truePeakOut,truePeakPosOut,shortTermMaxOut,momentaryMaxOut,shortTermMaxPosOut,momentaryMaxPosOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Boolean analyzeTruePeak, Float lufsIntegratedOut, Float rangeOut, Float  truePeakOut, Float truePeakPosOut, Float shortTermMaxOut, Float momentaryMaxOut, Float shortTermMaxPosOut, Float momentaryMaxPosOut) = NF_AnalyzeTakeLoudness2(take, analyzeTruePeak, lufsIntegratedOut, rangeOut,  truePeakOut, truePeakPosOut, shortTermMaxOut, momentaryMaxOut, shortTermMaxPosOut, momentaryMaxPosOut)
    
    Same as NF_AnalyzeTakeLoudness
     but additionally returns shortTermMaxPos and momentaryMaxPos which can be jumped to with SetEditCurPos(). Note: shortTermMaxPos and momentaryMaxPos actaully indicate the beginning of time  intervalls
    , (3 sec. and 0.4 sec. resp.).
    """
    a=rpr_getfp('NF_AnalyzeTakeLoudness2')
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(analyzeTruePeak),c_double(lufsIntegratedOut),c_double(rangeOut),c_double(truePeakOut),c_double(truePeakPosOut),c_double(shortTermMaxOut),c_double(momentaryMaxOut),c_double(shortTermMaxPosOut),c_double(momentaryMaxPosOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]),byref(t[9]))
    return (r,take,analyzeTruePeak,float(t[2].value),float(t[3].value),float(t[4].value),float(t[5].value),float(t[6].value),float(t[7].value),float(t[8].value),float(t[9].value))
     
def NF_AnalyzeTakeLoudness_IntegratedOnly(take,lufsIntegratedOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Float lufsIntegratedOut) = NF_AnalyzeTakeLoudness_IntegratedOnly(take, lufsIntegratedOut)
    
    Does LUFS integrated analysis only. Faster than full loudness analysis (NF_AnalyzeTakeLoudness
    ) . Use this if only LUFS integrated is required.
    """
    a=rpr_getfp('NF_AnalyzeTakeLoudness_IntegratedOnly')
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(lufsIntegratedOut))
    r=f(t[0],byref(t[1]))
    return (r,take,float(t[1].value))
     
def NF_GetMediaItemAverageRMS(item):
    """
    Python: Float  NF_GetMediaItemAverageRMS(MediaItem item)
    
    Returns the average overall (non-windowed) RMS level of active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX. 
    
     Returns -150.0 if MIDI take or empty item.
    """
    a=rpr_getfp('NF_GetMediaItemAverageRMS')
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def NF_GetMediaItemMaxPeak(item):
    """
    Python: Float  NF_GetMediaItemMaxPeak(MediaItem item)
    
    Returns the greatest max. peak value of all active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX. 
    
     Returns -150.0 if MIDI take or empty item.
    """
    a=rpr_getfp('NF_GetMediaItemMaxPeak')
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def NF_GetMediaItemPeakRMS_NonWindowed(item):
    """
    Python: Float  NF_GetMediaItemPeakRMS_NonWindowed(MediaItem item)
    
    Returns the greatest overall (non-windowed) RMS peak level of all active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX. 
    
     Returns -150.0 if MIDI take or empty item.
    """
    a=rpr_getfp('NF_GetMediaItemPeakRMS_NonWindowed')
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def NF_GetMediaItemPeakRMS_Windowed(item):
    """
    Python: Float  NF_GetMediaItemPeakRMS_Windowed(MediaItem item)
    
    Returns the average RMS peak level of all active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX. 
    
     Obeys 'Window size for peak RMS' setting in 'SWS: Set RMS analysis/normalize options' for calculation. Returns -150.0 if MIDI take or empty item.
    """
    a=rpr_getfp('NF_GetMediaItemPeakRMS_Windowed')
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def SN_FocusMIDIEditor():
    """
    Python: SN_FocusMIDIEditor()
    
    Focuses the active/open MIDI editor.
    """
    a=rpr_getfp('SN_FocusMIDIEditor')
    f=CFUNCTYPE(None)(a)
    f()
     
def SNM_AddReceive(src,dest,Type):
    """
    Python: Boolean  SNM_AddReceive(MediaTrack src, MediaTrack dest, Int type)
    
    [S&M] Deprecated, see CreateTrackSend
     (v5.15pre1+). Adds a receive. Returns false if nothing updated.
    
    type -1=Default type (user preferences), 0=Post-Fader (Post-Pan), 1=Pre-FX, 2=deprecated, 3=Pre-Fader (Post-FX).
    
    Note: obeys default sends preferences, supports frozen tracks, etc..
    """
    a=rpr_getfp('SNM_AddReceive')
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',src),rpr_packp('MediaTrack*',dest),c_int(Type))
    r=f(t[0],t[1],t[2])
    return r
     
def SNM_AddTCPFXParm(tr,fxId,prmId):
    """
    Python: Boolean  SNM_AddTCPFXParm(MediaTrack tr, Int fxId, Int prmId)
    
    [S&M] Add an FX parameter knob in the TCP. Returns false if nothing updated (invalid parameters, knob already present, etc..)
    """
    a=rpr_getfp('SNM_AddTCPFXParm')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(fxId),c_int(prmId))
    r=f(t[0],t[1],t[2])
    return r
     
def SNM_CreateFastString(Str):
    """
    Python: WDL_FastString  SNM_CreateFastString(String str)
    
    [S&M] Instantiates a new "fast string". You must delete this string, see SNM_DeleteFastString
    .
    """
    a=rpr_getfp('SNM_CreateFastString')
    f=CFUNCTYPE(c_uint64,c_char_p)(a)
    t=(rpr_packsc(Str),)
    r=f(t[0])
    return rpr_unpackp('WDL_FastString*',r)
     
def SNM_DeleteFastString(Str):
    """
    Python: SNM_DeleteFastString(WDL_FastString str)
    
    [S&M] Deletes a "fast string" instance.
    """
    a=rpr_getfp('SNM_DeleteFastString')
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('WDL_FastString*',Str),)
    f(t[0])
     
def SNM_GetDoubleConfigVar(varname,errvalue):
    """
    Python: Float  SNM_GetDoubleConfigVar(String varname, Float errvalue)
    
    [S&M] Returns a double preference (look in project prefs first, then in general prefs). Returns errvalue if failed (e.g. varname not found).
    """
    a=rpr_getfp('SNM_GetDoubleConfigVar')
    f=CFUNCTYPE(c_double,c_char_p,c_double)(a)
    t=(rpr_packsc(varname),c_double(errvalue))
    r=f(t[0],t[1])
    return r
     
def SNM_GetFastString(Str):
    """
    Python: String  SNM_GetFastString(WDL_FastString str)
    
    [S&M] Gets the "fast string" content.
    """
    a=rpr_getfp('SNM_GetFastString')
    f=CFUNCTYPE(c_char_p,c_uint64)(a)
    t=(rpr_packp('WDL_FastString*',Str),)
    r=f(t[0])
    return str(r.decode())
     
def SNM_GetFastStringLength(Str):
    """
    Python: Int  SNM_GetFastStringLength(WDL_FastString str)
    
    [S&M] Gets the "fast string" length.
    """
    a=rpr_getfp('SNM_GetFastStringLength')
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('WDL_FastString*',Str),)
    r=f(t[0])
    return r
     
def SNM_GetIntConfigVar(varname,errvalue):
    """
    Python: Int  SNM_GetIntConfigVar(String varname, Int errvalue)
    
    [S&M] Returns an integer preference (look in project prefs first, then in general prefs). Returns errvalue if failed (e.g. varname not found).
    """
    a=rpr_getfp('SNM_GetIntConfigVar')
    f=CFUNCTYPE(c_int,c_char_p,c_int)(a)
    t=(rpr_packsc(varname),c_int(errvalue))
    r=f(t[0],t[1])
    return r
     
def SNM_GetMediaItemTakeByGUID(project,guid):
    """
    Python: MediaItem_Take  SNM_GetMediaItemTakeByGUID(ReaProject project, String guid)
    
    [S&M] Gets a take by GUID as string. The GUID must be enclosed in braces {}. To get take GUID as string, see BR_GetMediaItemTakeGUID
    """
    a=rpr_getfp('SNM_GetMediaItemTakeByGUID')
    f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('ReaProject*',project),rpr_packsc(guid))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem_Take*',r)
     
def SNM_GetProjectMarkerName(proj,num,isrgn,name):
    """
    Python: Boolean  SNM_GetProjectMarkerName(ReaProject proj, Int num, Boolean isrgn, WDL_FastString name)
    
    [S&M] Gets a marker/region name. Returns true if marker/region found.
    """
    a=rpr_getfp('SNM_GetProjectMarkerName')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(num),c_byte(isrgn),rpr_packp('WDL_FastString*',name))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def SNM_GetSetObjectState(obj,state,setnewvalue,wantminimalstate):
    """
    Python: Boolean  SNM_GetSetObjectState(void obj, WDL_FastString state, Boolean setnewvalue, Boolean wantminimalstate)
    
    [S&M] Gets or sets the state of a track, an item or an envelope. The state chunk size is unlimited. Returns false if failed.
    
    When getting a track state (and when you are not interested in FX data), you can use wantminimalstate=true to radically reduce the length of the state. Do not set such minimal states back though, this is for read-only applications!
    
    Note: unlike the native GetSetObjectState, calling to FreeHeapPtr() is not required.
    """
    a=rpr_getfp('SNM_GetSetObjectState')
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_byte,c_byte)(a)
    t=(rpr_packp('void*',obj),rpr_packp('WDL_FastString*',state),c_byte(setnewvalue),c_byte(wantminimalstate))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def SNM_GetSetSourceState(item,takeidx,state,setnewvalue):
    """
    Python: Boolean  SNM_GetSetSourceState(MediaItem item, Int takeidx, WDL_FastString state, Boolean setnewvalue)
    
    [S&M] Gets or sets a take source state. Returns false if failed. Use takeidx=-1 to get/alter the active take.
    
    Note: this function does not use a MediaItem_Take* param in order to manage empty takes (i.e. takes with MediaItem_Take*==NULL), see SNM_GetSetSourceState2
    .
    """
    a=rpr_getfp('SNM_GetSetSourceState')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),c_int(takeidx),rpr_packp('WDL_FastString*',state),c_byte(setnewvalue))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def SNM_GetSetSourceState2(take,state,setnewvalue):
    """
    Python: Boolean  SNM_GetSetSourceState2(MediaItem_Take take, WDL_FastString state, Boolean setnewvalue)
    
    [S&M] Gets or sets a take source state. Returns false if failed.
    
    Note: this function cannot deal with empty takes, see SNM_GetSetSourceState
    .
    """
    a=rpr_getfp('SNM_GetSetSourceState2')
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packp('WDL_FastString*',state),c_byte(setnewvalue))
    r=f(t[0],t[1],t[2])
    return r
     
def SNM_GetSourceType(take,Type):
    """
    Python: Boolean  SNM_GetSourceType(MediaItem_Take take, WDL_FastString type)
    
    [S&M] Gets the source type of a take. Returns false if failed (e.g. take with empty source, etc..)
    """
    a=rpr_getfp('SNM_GetSourceType')
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packp('WDL_FastString*',Type))
    r=f(t[0],t[1])
    return r
     
def SNM_MoveOrRemoveTrackFX(tr,fxId,what):
    """
    Python: Boolean  SNM_MoveOrRemoveTrackFX(MediaTrack tr, Int fxId, Int what)
    
    [S&M] Move or removes a track FX. Returns true if tr has been updated.
    
    fxId: fx index in chain or -1 for the selected fx. what: 0 to remove, -1 to move fx up in chain, 1 to move fx down in chain.
    """
    a=rpr_getfp('SNM_MoveOrRemoveTrackFX')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(fxId),c_int(what))
    r=f(t[0],t[1],t[2])
    return r
     
def SNM_ReadMediaFileTag(fn,tag,tagval,tagval_sz):
    """
    Python: (Boolean retval, String fn, String tag, String tagval, Int tagval_sz) = SNM_ReadMediaFileTag(fn, tag, tagval, tagval_sz)
    
    [S&M] Reads a media file tag. Supported tags: "artist", "album", "genre", "comment", "title", or "year". Returns false if tag was not found. See SNM_TagMediaFile
    .
    """
    a=rpr_getfp('SNM_ReadMediaFileTag')
    f=CFUNCTYPE(c_byte,c_char_p,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(fn),rpr_packsc(tag),rpr_packs(tagval),c_int(tagval_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,fn,tag,rpr_unpacks(t[2]),tagval_sz)
     
def SNM_RemoveReceive(tr,rcvidx):
    """
    Python: Boolean  SNM_RemoveReceive(MediaTrack tr, Int rcvidx)
    
    [S&M] Deprecated, see RemoveTrackSend
     (v5.15pre1+). Removes a receive. Returns false if nothing updated.
    """
    a=rpr_getfp('SNM_RemoveReceive')
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(rcvidx))
    r=f(t[0],t[1])
    return r
     
def SNM_RemoveReceivesFrom(tr,srctr):
    """
    Python: Boolean  SNM_RemoveReceivesFrom(MediaTrack tr, MediaTrack srctr)
    
    [S&M] Removes all receives from srctr. Returns false if nothing updated.
    """
    a=rpr_getfp('SNM_RemoveReceivesFrom')
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packp('MediaTrack*',srctr))
    r=f(t[0],t[1])
    return r
     
def SNM_SelectResourceBookmark(name):
    """
    Python: Int  SNM_SelectResourceBookmark(String name)
    
    [S&M] Select a bookmark of the Resources window. Returns the related bookmark id (or -1 if failed).
    """
    a=rpr_getfp('SNM_SelectResourceBookmark')
    f=CFUNCTYPE(c_int,c_char_p)(a)
    t=(rpr_packsc(name),)
    r=f(t[0])
    return r
     
def SNM_SetDoubleConfigVar(varname,newvalue):
    """
    Python: Boolean  SNM_SetDoubleConfigVar(String varname, Float newvalue)
    
    [S&M] Sets a double preference (look in project prefs first, then in general prefs). Returns false if failed (e.g. varname not found).
    """
    a=rpr_getfp('SNM_SetDoubleConfigVar')
    f=CFUNCTYPE(c_byte,c_char_p,c_double)(a)
    t=(rpr_packsc(varname),c_double(newvalue))
    r=f(t[0],t[1])
    return r
     
def SNM_SetFastString(Str,newstr):
    """
    Python: WDL_FastString  SNM_SetFastString(WDL_FastString str, String newstr)
    
    [S&M] Sets the "fast string" content. Returns str for facility.
    """
    a=rpr_getfp('SNM_SetFastString')
    f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('WDL_FastString*',Str),rpr_packsc(newstr))
    r=f(t[0],t[1])
    return rpr_unpackp('WDL_FastString*',r)
     
def SNM_SetIntConfigVar(varname,newvalue):
    """
    Python: Boolean  SNM_SetIntConfigVar(String varname, Int newvalue)
    
    [S&M] Sets an integer preference (look in project prefs first, then in general prefs). Returns false if failed (e.g. varname not found).
    """
    a=rpr_getfp('SNM_SetIntConfigVar')
    f=CFUNCTYPE(c_byte,c_char_p,c_int)(a)
    t=(rpr_packsc(varname),c_int(newvalue))
    r=f(t[0],t[1])
    return r
     
def SNM_SetProjectMarker(proj,num,isrgn,pos,rgnend,name,color):
    """
    Python: Boolean  SNM_SetProjectMarker(ReaProject proj, Int num, Boolean isrgn, Float pos, Float rgnend, String name, Int color)
    
    [S&M] Deprecated, see SetProjectMarker4
     -- Same function as SetProjectMarker3() except it can set empty names "".
    """
    a=rpr_getfp('SNM_SetProjectMarker')
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_double,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(num),c_byte(isrgn),c_double(pos),c_double(rgnend),rpr_packsc(name),c_int(color))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return r
     
def SNM_TagMediaFile(fn,tag,tagval):
    """
    Python: Boolean  SNM_TagMediaFile(String fn, String tag, String tagval)
    
    [S&M] Tags a media file thanks to TagLib
    . Supported tags: "artist", "album", "genre", "comment", "title", or "year". Use an empty tagval to clear a tag. When a file is opened in REAPER, turn it offline before using this function. Returns false if nothing updated. See SNM_ReadMediaFileTag
    .
    """
    a=rpr_getfp('SNM_TagMediaFile')
    f=CFUNCTYPE(c_byte,c_char_p,c_char_p,c_char_p)(a)
    t=(rpr_packsc(fn),rpr_packsc(tag),rpr_packsc(tagval))
    r=f(t[0],t[1],t[2])
    return r
     
def SNM_TieResourceSlotActions(bookmarkId):
    """
    Python: SNM_TieResourceSlotActions(Int bookmarkId)
    
    [S&M] Attach Resources slot actions to a given bookmark.
    """
    a=rpr_getfp('SNM_TieResourceSlotActions')
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(bookmarkId),)
    f(t[0])
     
def ULT_GetMediaItemNote(item):
    """
    Python: String  ULT_GetMediaItemNote(MediaItem item)
    
    [ULT] Get item notes.
    """
    a=rpr_getfp('ULT_GetMediaItemNote')
    f=CFUNCTYPE(c_char_p,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return str(r.decode())
     
def ULT_SetMediaItemNote(item,note):
    """
    Python: ULT_SetMediaItemNote(MediaItem item, String note)
    
    [ULT] Set item notes.
    """
    a=rpr_getfp('ULT_SetMediaItemNote')
    f=CFUNCTYPE(None,c_uint64,c_char_p)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packsc(note))
    f(t[0],t[1])
     
