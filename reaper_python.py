# REAPER 5.95


import re
from ctypes import *
 
# lowercase rpr_ functions are for internal use 
 
_ft={}
 
def rpr_initft(ft):
    if (len(_ft) == 0):
        _ft.update(ft)
         
def rpr_getfp(fn):
    return _ft[fn]
     
def rpr_packp(t,v):
    m=re.match('^\((\w+\*|HWND)\)0x([0-9A-F]+)$', str(v))
    if (m != None):
        (_t,_v)=m.groups()
        if (_t == t or t == 'void*'):
            a=int(_v[:8],16)
            b=int(_v[8:],16);
            p=c_uint64((a<<32)|b).value
            if (RPR_ValidatePtr(p,t)):
                return p
    return 0
     
def rpr_unpackp(t,v):
    if (v == None):
        v=0
    a=int(v>>32)
    b=int(v&0xFFFFFFFF)
    return '(%s)0x%08X%08X' % (t,a,b)
     
def RPR_ValidatePtr(p,t):
    """
    Python: Boolean  RPR_ValidatePtr(void pointer, String ctypename)
    
    see ValidatePtr2
    """
    a=_ft['ValidatePtr']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p)(a)
    return f(c_uint64(p),rpr_packsc(t))
     
def rpr_packsc(v):
    return c_char_p(str(v).encode())
     
def rpr_packs(v):
    MAX_STRBUF=4*1024*1024
    return create_string_buffer(str(v).encode(),MAX_STRBUF)
     
def rpr_unpacks(v):
    return str(v.value.decode())
     
def RPR_GetAudioAccessorSamples(accessor,samplerate,numchannels,starttime_sec,numsamplesperchannel,samplebuffer):
    """
    Python: (Int retval, AudioAccessor accessor, Int samplerate, Int numchannels, Float starttime_sec, Int numsamplesperchannel, Float samplebuffer) = RPR_GetAudioAccessorSamples(accessor, samplerate, numchannels, starttime_sec, numsamplesperchannel, samplebuffer)
    
    Get a block of samples from the audio accessor. Samples are extracted immediately pre-FX, and returned interleaved (first sample of first channel, first sample of second channel...). Returns 0 if no audio, 1 if audio, -1 on error. See CreateTakeAudioAccessor
    , CreateTrackAudioAccessor
    , DestroyAudioAccessor
    , GetAudioAccessorHash
    , GetAudioAccessorStartTime
    , GetAudioAccessorEndTime
    .
    
    
    This function has special handling in Python, and only returns two objects, the API function return value, and the sample buffer. Example usage:
    
    tr = RPR_GetTrack(0, 0)
    aa = RPR_CreateTrackAudioAccessor(tr)
    buf = list([0]*2*1024) # 2 channels, 1024 samples each, initialized to zero
    pos = 0.0
    (ret, buf) = GetAudioAccessorSamples(aa, 44100, 2, pos, 1024, buf)
    # buf now holds the first 2*1024 audio samples from the track.
    # typically GetAudioAccessorSamples() would be called within a loop, increasing pos each time.
    """
    a=_ft['GetAudioAccessorSamples']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_int,c_double,c_int,c_void_p)(a)
    v=cast((c_double*numchannels*numsamplesperchannel)(),POINTER(c_double))
    t=(rpr_packp('void*',accessor),c_int(samplerate),c_int(numchannels),c_double(starttime_sec),c_int(numsamplesperchannel),v)
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    for i in range(numchannels*numsamplesperchannel):
        samplebuffer[i]=float(v[i])
    return (r,samplebuffer)
     
def RPR_AddMediaItemToTrack(tr):
    """
    Python: MediaItem  RPR_AddMediaItemToTrack(MediaTrack tr)
    
    creates a new media item.
    """
    a=_ft['AddMediaItemToTrack']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),)
    r=f(t[0])
    return rpr_unpackp('MediaItem*',r)
     
def RPR_AddProjectMarker(proj,isrgn,pos,rgnend,name,wantidx):
    """
    Python: Int  RPR_AddProjectMarker(ReaProject proj, Boolean isrgn, Float pos, Float rgnend, String name, Int wantidx)
    
    Returns the index of the created marker/region, or -1 on failure. Supply wantidx>=0 if you want a particular index number, but you'll get a different index number a region and wantidx is already in use.
    """
    a=_ft['AddProjectMarker']
    f=CFUNCTYPE(c_int,c_uint64,c_byte,c_double,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(isrgn),c_double(pos),c_double(rgnend),rpr_packsc(name),c_int(wantidx))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def RPR_AddProjectMarker2(proj,isrgn,pos,rgnend,name,wantidx,color):
    """
    Python: Int  RPR_AddProjectMarker2(ReaProject proj, Boolean isrgn, Float pos, Float rgnend, String name, Int wantidx, Int color)
    
    Returns the index of the created marker/region, or -1 on failure. Supply wantidx>=0 if you want a particular index number, but you'll get a different index number a region and wantidx is already in use. color should be 0 (default color), or ColorToNative(r,g,b)|0x1000000
    """
    a=_ft['AddProjectMarker2']
    f=CFUNCTYPE(c_int,c_uint64,c_byte,c_double,c_double,c_char_p,c_int,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(isrgn),c_double(pos),c_double(rgnend),rpr_packsc(name),c_int(wantidx),c_int(color))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return r
     
def RPR_AddRemoveReaScript(add,sectionID,scriptfn,commit):
    """
    Python: Int  RPR_AddRemoveReaScript(Boolean add, Int sectionID, String scriptfn, Boolean commit)
    
    Add a ReaScript (return the new command ID, or 0 if failed) or remove a ReaScript (return >0 on success). Use commit==true when adding/removing a single script. When bulk adding/removing n scripts, you can optimize the n-1 first calls with commit==false and commit==true for the last call.
    """
    a=_ft['AddRemoveReaScript']
    f=CFUNCTYPE(c_int,c_byte,c_int,c_char_p,c_byte)(a)
    t=(c_byte(add),c_int(sectionID),rpr_packsc(scriptfn),c_byte(commit))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_AddTakeToMediaItem(item):
    """
    Python: MediaItem_Take  RPR_AddTakeToMediaItem(MediaItem item)
    
    creates a new take in an item
    """
    a=_ft['AddTakeToMediaItem']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return rpr_unpackp('MediaItem_Take*',r)
     
def RPR_AddTempoTimeSigMarker(proj,timepos,bpm,timesig_num,timesig_denom,lineartempochange):
    """
    Python: Boolean  RPR_AddTempoTimeSigMarker(ReaProject proj, Float timepos, Float bpm, Int timesig_num, Int timesig_denom, Boolean lineartempochange)
    
    Deprecated. Use SetTempoTimeSigMarker with ptidx=-1.
    """
    a=_ft['AddTempoTimeSigMarker']
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_double,c_int,c_int,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(timepos),c_double(bpm),c_int(timesig_num),c_int(timesig_denom),c_byte(lineartempochange))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def RPR_adjustZoom(amt,forceset,doupd,centermode):
    """
    Python: RPR_adjustZoom(Float amt, Int forceset, Boolean doupd, Int centermode)
    
    forceset=0,doupd=true,centermode=-1 for default
    """
    a=_ft['adjustZoom']
    f=CFUNCTYPE(None,c_double,c_int,c_byte,c_int)(a)
    t=(c_double(amt),c_int(forceset),c_byte(doupd),c_int(centermode))
    f(t[0],t[1],t[2],t[3])
     
def RPR_AnyTrackSolo(proj):
    """
    Python: Boolean  RPR_AnyTrackSolo(ReaProject proj)
    """
    a=_ft['AnyTrackSolo']
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_APIExists(function_name):
    """
    Python: Boolean  RPR_APIExists(String function_name)
    
    Returns true if function_name exists in the REAPER API
    """
    a=_ft['APIExists']
    f=CFUNCTYPE(c_byte,c_char_p)(a)
    t=(rpr_packsc(function_name),)
    r=f(t[0])
    return r
     
def RPR_APITest():
    """
    Python: RPR_APITest()
    
    Displays a message window if the API was successfully called.
    """
    a=_ft['APITest']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_ApplyNudge(project,nudgeflag,nudgewhat,nudgeunits,value,reverse,copies):
    """
    Python: Boolean  RPR_ApplyNudge(ReaProject project, Int nudgeflag, Int nudgewhat, Int nudgeunits, Float value, Boolean reverse, Int copies)
    
    nudgeflag: &1=set to value (otherwise nudge by value), &2=snap
    
    nudgewhat: 0=position, 1=left trim, 2=left edge, 3=right edge, 4=contents, 5=duplicate, 6=edit cursor
    
    nudgeunit: 0=ms, 1=seconds, 2=grid, 3=256th notes, ..., 15=whole notes, 16=measures.beats (1.15 = 1 measure + 1.5 beats), 17=samples, 18=frames, 19=pixels, 20=item lengths, 21=item selections
    
    value: amount to nudge by, or value to set to
    
    reverse: in nudge mode, nudges left (otherwise ignored)
    
    copies: in nudge duplicate mode, number of copies (otherwise ignored)
    """
    a=_ft['ApplyNudge']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_int,c_double,c_byte,c_int)(a)
    t=(rpr_packp('ReaProject*',project),c_int(nudgeflag),c_int(nudgewhat),c_int(nudgeunits),c_double(value),c_byte(reverse),c_int(copies))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return r
     
def RPR_ArmCommand(cmd,sectionname):
    """
    Python: RPR_ArmCommand(Int cmd, String sectionname)
    
    arms a command (or disarms if 0 passed) in section sectionname (empty string for main)
    """
    a=_ft['ArmCommand']
    f=CFUNCTYPE(None,c_int,c_char_p)(a)
    t=(c_int(cmd),rpr_packsc(sectionname))
    f(t[0],t[1])
     
def RPR_Audio_Init():
    """
    Python: RPR_Audio_Init()
    
    open all audio and MIDI devices, if not open
    """
    a=_ft['Audio_Init']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_Audio_IsPreBuffer():
    """
    Python: Int  RPR_Audio_IsPreBuffer()
    
    is in pre-buffer? threadsafe
    """
    a=_ft['Audio_IsPreBuffer']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_Audio_IsRunning():
    """
    Python: Int  RPR_Audio_IsRunning()
    
    is audio running at all? threadsafe
    """
    a=_ft['Audio_IsRunning']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_Audio_Quit():
    """
    Python: RPR_Audio_Quit()
    
    close all audio and MIDI devices, if open
    """
    a=_ft['Audio_Quit']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_AudioAccessorValidateState(accessor):
    """
    Python: Boolean  RPR_AudioAccessorValidateState(AudioAccessor accessor)
    
    Validates the current state of the audio accessor -- must ONLY call this from the main thread. Returns true if the state changed.
    """
    a=_ft['AudioAccessorValidateState']
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('AudioAccessor*',accessor),)
    r=f(t[0])
    return r
     
def RPR_BypassFxAllTracks(bypass):
    """
    Python: RPR_BypassFxAllTracks(Int bypass)
    
    -1 = bypass all if not all bypassed,otherwise unbypass all
    """
    a=_ft['BypassFxAllTracks']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(bypass),)
    f(t[0])
     
def RPR_ClearAllRecArmed():
    """
    Python: RPR_ClearAllRecArmed()
    """
    a=_ft['ClearAllRecArmed']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_ClearConsole():
    """
    Python: RPR_ClearConsole()
    
    Clear the ReaScript console. See ShowConsoleMsg
    """
    a=_ft['ClearConsole']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_ClearPeakCache():
    """
    Python: RPR_ClearPeakCache()
    
    resets the global peak caches
    """
    a=_ft['ClearPeakCache']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_ColorFromNative(col,rOut,gOut,bOut):
    """
    Python: (Int col, Int rOut, Int gOut, Int bOut) = RPR_ColorFromNative(col, rOut, gOut, bOut)
    
    Extract RGB values from an OS dependent color. See ColorToNative
    .
    """
    a=_ft['ColorFromNative']
    f=CFUNCTYPE(None,c_int,c_void_p,c_void_p,c_void_p)(a)
    t=(c_int(col),c_int(rOut),c_int(gOut),c_int(bOut))
    f(t[0],byref(t[1]),byref(t[2]),byref(t[3]))
    return (col,int(t[1].value),int(t[2].value),int(t[3].value))
     
def RPR_ColorToNative(r,g,b):
    """
    Python: Int  RPR_ColorToNative(Int r, Int g, Int b)
    
    Make an OS dependent color from RGB values (e.g. RGB() macro on Windows). r,g and b are in [0..255]. See ColorFromNative
    .
    """
    a=_ft['ColorToNative']
    f=CFUNCTYPE(c_int,c_int,c_int,c_int)(a)
    t=(c_int(r),c_int(g),c_int(b))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CountAutomationItems(env):
    """
    Python: Int  RPR_CountAutomationItems(TrackEnvelope env)
    
    Returns the number of automation items on this envelope. See GetSetAutomationItemInfo
    """
    a=_ft['CountAutomationItems']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('TrackEnvelope*',env),)
    r=f(t[0])
    return r
     
def RPR_CountEnvelopePoints(envelope):
    """
    Python: Int  RPR_CountEnvelopePoints(TrackEnvelope envelope)
    
    Returns the number of points in the envelope.
    """
    a=_ft['CountEnvelopePoints']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),)
    r=f(t[0])
    return r
     
def RPR_CountEnvelopePointsEx(envelope,autoitem_idx):
    """
    Python: Int  RPR_CountEnvelopePointsEx(TrackEnvelope envelope, Int autoitem_idx)
    
    Returns the number of points in the envelope. autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc.
    """
    a=_ft['CountEnvelopePointsEx']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(autoitem_idx))
    r=f(t[0],t[1])
    return r
     
def RPR_CountMediaItems(proj):
    """
    Python: Int  RPR_CountMediaItems(ReaProject proj)
    
    count the number of items in the project (proj=0 for active project)
    """
    a=_ft['CountMediaItems']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_CountProjectMarkers(proj,num_markersOut,num_regionsOut):
    """
    Python: (Int retval, ReaProject proj, Int num_markersOut, Int num_regionsOut) = RPR_CountProjectMarkers(proj, num_markersOut, num_regionsOut)
    
    num_markersOut and num_regionsOut may be NULL.
    """
    a=_ft['CountProjectMarkers']
    f=CFUNCTYPE(c_int,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(num_markersOut),c_int(num_regionsOut))
    r=f(t[0],byref(t[1]),byref(t[2]))
    return (r,proj,int(t[1].value),int(t[2].value))
     
def RPR_CountSelectedMediaItems(proj):
    """
    Python: Int  RPR_CountSelectedMediaItems(ReaProject proj)
    
    count the number of selected items in the project (proj=0 for active project)
    """
    a=_ft['CountSelectedMediaItems']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_CountSelectedTracks(proj):
    """
    Python: Int  RPR_CountSelectedTracks(ReaProject proj)
    
    Count the number of selected tracks in the project (proj=0 for active project). This function ignores the master track, see CountSelectedTracks2
    .
    """
    a=_ft['CountSelectedTracks']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_CountSelectedTracks2(proj,wantmaster):
    """
    Python: Int  RPR_CountSelectedTracks2(ReaProject proj, Boolean wantmaster)
    
    Count the number of selected tracks in the project (proj=0 for active project).
    """
    a=_ft['CountSelectedTracks2']
    f=CFUNCTYPE(c_int,c_uint64,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(wantmaster))
    r=f(t[0],t[1])
    return r
     
def RPR_CountTakeEnvelopes(take):
    """
    Python: Int  RPR_CountTakeEnvelopes(MediaItem_Take take)
    
    See GetTakeEnvelope
    """
    a=_ft['CountTakeEnvelopes']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def RPR_CountTakes(item):
    """
    Python: Int  RPR_CountTakes(MediaItem item)
    
    count the number of takes in the item
    """
    a=_ft['CountTakes']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def RPR_CountTCPFXParms(project,track):
    """
    Python: Int  RPR_CountTCPFXParms(ReaProject project, MediaTrack track)
    
    Count the number of FX parameter knobs displayed on the track control panel.
    """
    a=_ft['CountTCPFXParms']
    f=CFUNCTYPE(c_int,c_uint64,c_uint64)(a)
    t=(rpr_packp('ReaProject*',project),rpr_packp('MediaTrack*',track))
    r=f(t[0],t[1])
    return r
     
def RPR_CountTempoTimeSigMarkers(proj):
    """
    Python: Int  RPR_CountTempoTimeSigMarkers(ReaProject proj)
    
    Count the number of tempo/time signature markers in the project. See GetTempoTimeSigMarker
    , SetTempoTimeSigMarker
    , AddTempoTimeSigMarker
    .
    """
    a=_ft['CountTempoTimeSigMarkers']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_CountTrackEnvelopes(track):
    """
    Python: Int  RPR_CountTrackEnvelopes(MediaTrack track)
    
    see GetTrackEnvelope
    """
    a=_ft['CountTrackEnvelopes']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_CountTrackMediaItems(track):
    """
    Python: Int  RPR_CountTrackMediaItems(MediaTrack track)
    
    count the number of items in the track
    """
    a=_ft['CountTrackMediaItems']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_CountTracks(proj):
    """
    Python: Int  RPR_CountTracks(ReaProject proj)
    
    count the number of tracks in the project (proj=0 for active project)
    """
    a=_ft['CountTracks']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_CreateNewMIDIItemInProj(track,starttime,endtime,qnInOptional):
    """
    Python: MediaItem  RPR_CreateNewMIDIItemInProj(MediaTrack track, Float starttime, Float endtime, const bool qnInOptional)
    
    Create a new MIDI media item, containing no MIDI events. Time is in seconds unless qn is set.
    """
    a=_ft['CreateNewMIDIItemInProj']
    f=CFUNCTYPE(c_uint64,c_uint64,c_double,c_double,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_double(starttime),c_double(endtime),c_byte(qnInOptional))
    r=f(t[0],t[1],t[2],byref(t[3]))
    return (rpr_unpackp('MediaItem*',r),track,starttime,endtime,int(t[3].value))
     
def RPR_CreateTakeAudioAccessor(take):
    """
    Python: AudioAccessor  RPR_CreateTakeAudioAccessor(MediaItem_Take take)
    
    Create an audio accessor object for this take. Must only call from the main thread. See CreateTrackAudioAccessor
    , DestroyAudioAccessor
    , GetAudioAccessorHash
    , GetAudioAccessorStartTime
    , GetAudioAccessorEndTime
    , GetAudioAccessorSamples
    .
    """
    a=_ft['CreateTakeAudioAccessor']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return rpr_unpackp('AudioAccessor*',r)
     
def RPR_CreateTrackAudioAccessor(track):
    """
    Python: AudioAccessor  RPR_CreateTrackAudioAccessor(MediaTrack track)
    
    Create an audio accessor object for this track. Must only call from the main thread. See CreateTakeAudioAccessor
    , DestroyAudioAccessor
    , GetAudioAccessorHash
    , GetAudioAccessorStartTime
    , GetAudioAccessorEndTime
    , GetAudioAccessorSamples
    .
    """
    a=_ft['CreateTrackAudioAccessor']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return rpr_unpackp('AudioAccessor*',r)
     
def RPR_CreateTrackSend(tr,desttrInOptional):
    """
    Python: Int  RPR_CreateTrackSend(MediaTrack tr, MediaTrack desttrInOptional)
    
    Create a send/receive (desttrInOptional!=NULL), or a hardware output (desttrInOptional==NULL) with default properties, return >=0 on success (== new send/receive index). See RemoveTrackSend
    , GetSetTrackSendInfo
    , GetTrackSendInfo_Value
    , SetTrackSendInfo_Value
    .
    """
    a=_ft['CreateTrackSend']
    f=CFUNCTYPE(c_int,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packp('MediaTrack*',desttrInOptional))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_FlushUndo(force):
    """
    Python: RPR_CSurf_FlushUndo(Boolean force)
    
    call this to force flushing of the undo states after using CSurf_On*Change()
    """
    a=_ft['CSurf_FlushUndo']
    f=CFUNCTYPE(None,c_byte)(a)
    t=(c_byte(force),)
    f(t[0])
     
def RPR_CSurf_GetTouchState(trackid,isPan):
    """
    Python: Boolean  RPR_CSurf_GetTouchState(MediaTrack trackid, Int isPan)
    """
    a=_ft['CSurf_GetTouchState']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(isPan))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_GoEnd():
    """
    Python: RPR_CSurf_GoEnd()
    """
    a=_ft['CSurf_GoEnd']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_GoStart():
    """
    Python: RPR_CSurf_GoStart()
    """
    a=_ft['CSurf_GoStart']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_NumTracks(mcpView):
    """
    Python: Int  RPR_CSurf_NumTracks(Boolean mcpView)
    """
    a=_ft['CSurf_NumTracks']
    f=CFUNCTYPE(c_int,c_byte)(a)
    t=(c_byte(mcpView),)
    r=f(t[0])
    return r
     
def RPR_CSurf_OnArrow(whichdir,wantzoom):
    """
    Python: RPR_CSurf_OnArrow(Int whichdir, Boolean wantzoom)
    """
    a=_ft['CSurf_OnArrow']
    f=CFUNCTYPE(None,c_int,c_byte)(a)
    t=(c_int(whichdir),c_byte(wantzoom))
    f(t[0],t[1])
     
def RPR_CSurf_OnFwd(seekplay):
    """
    Python: RPR_CSurf_OnFwd(Int seekplay)
    """
    a=_ft['CSurf_OnFwd']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(seekplay),)
    f(t[0])
     
def RPR_CSurf_OnFXChange(trackid,en):
    """
    Python: Boolean  RPR_CSurf_OnFXChange(MediaTrack trackid, Int en)
    """
    a=_ft['CSurf_OnFXChange']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(en))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_OnInputMonitorChange(trackid,monitor):
    """
    Python: Int  RPR_CSurf_OnInputMonitorChange(MediaTrack trackid, Int monitor)
    """
    a=_ft['CSurf_OnInputMonitorChange']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(monitor))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_OnInputMonitorChangeEx(trackid,monitor,allowgang):
    """
    Python: Int  RPR_CSurf_OnInputMonitorChangeEx(MediaTrack trackid, Int monitor, Boolean allowgang)
    """
    a=_ft['CSurf_OnInputMonitorChangeEx']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(monitor),c_byte(allowgang))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CSurf_OnMuteChange(trackid,mute):
    """
    Python: Boolean  RPR_CSurf_OnMuteChange(MediaTrack trackid, Int mute)
    """
    a=_ft['CSurf_OnMuteChange']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(mute))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_OnMuteChangeEx(trackid,mute,allowgang):
    """
    Python: Boolean  RPR_CSurf_OnMuteChangeEx(MediaTrack trackid, Int mute, Boolean allowgang)
    """
    a=_ft['CSurf_OnMuteChangeEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(mute),c_byte(allowgang))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CSurf_OnPanChange(trackid,pan,relative):
    """
    Python: Float  RPR_CSurf_OnPanChange(MediaTrack trackid, Float pan, Boolean relative)
    """
    a=_ft['CSurf_OnPanChange']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(pan),c_byte(relative))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CSurf_OnPanChangeEx(trackid,pan,relative,allowGang):
    """
    Python: Float  RPR_CSurf_OnPanChangeEx(MediaTrack trackid, Float pan, Boolean relative, Boolean allowGang)
    """
    a=_ft['CSurf_OnPanChangeEx']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_byte,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(pan),c_byte(relative),c_byte(allowGang))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_CSurf_OnPause():
    """
    Python: RPR_CSurf_OnPause()
    """
    a=_ft['CSurf_OnPause']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_OnPlay():
    """
    Python: RPR_CSurf_OnPlay()
    """
    a=_ft['CSurf_OnPlay']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_OnPlayRateChange(playrate):
    """
    Python: RPR_CSurf_OnPlayRateChange(Float playrate)
    """
    a=_ft['CSurf_OnPlayRateChange']
    f=CFUNCTYPE(None,c_double)(a)
    t=(c_double(playrate),)
    f(t[0])
     
def RPR_CSurf_OnRecArmChange(trackid,recarm):
    """
    Python: Boolean  RPR_CSurf_OnRecArmChange(MediaTrack trackid, Int recarm)
    """
    a=_ft['CSurf_OnRecArmChange']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(recarm))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_OnRecArmChangeEx(trackid,recarm,allowgang):
    """
    Python: Boolean  RPR_CSurf_OnRecArmChangeEx(MediaTrack trackid, Int recarm, Boolean allowgang)
    """
    a=_ft['CSurf_OnRecArmChangeEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(recarm),c_byte(allowgang))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CSurf_OnRecord():
    """
    Python: RPR_CSurf_OnRecord()
    """
    a=_ft['CSurf_OnRecord']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_OnRecvPanChange(trackid,recv_index,pan,relative):
    """
    Python: Float  RPR_CSurf_OnRecvPanChange(MediaTrack trackid, Int recv_index, Float pan, Boolean relative)
    """
    a=_ft['CSurf_OnRecvPanChange']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(recv_index),c_double(pan),c_byte(relative))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_CSurf_OnRecvVolumeChange(trackid,recv_index,volume,relative):
    """
    Python: Float  RPR_CSurf_OnRecvVolumeChange(MediaTrack trackid, Int recv_index, Float volume, Boolean relative)
    """
    a=_ft['CSurf_OnRecvVolumeChange']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(recv_index),c_double(volume),c_byte(relative))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_CSurf_OnRew(seekplay):
    """
    Python: RPR_CSurf_OnRew(Int seekplay)
    """
    a=_ft['CSurf_OnRew']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(seekplay),)
    f(t[0])
     
def RPR_CSurf_OnRewFwd(seekplay,Dir):
    """
    Python: RPR_CSurf_OnRewFwd(Int seekplay, Int dir)
    """
    a=_ft['CSurf_OnRewFwd']
    f=CFUNCTYPE(None,c_int,c_int)(a)
    t=(c_int(seekplay),c_int(Dir))
    f(t[0],t[1])
     
def RPR_CSurf_OnScroll(xdir,ydir):
    """
    Python: RPR_CSurf_OnScroll(Int xdir, Int ydir)
    """
    a=_ft['CSurf_OnScroll']
    f=CFUNCTYPE(None,c_int,c_int)(a)
    t=(c_int(xdir),c_int(ydir))
    f(t[0],t[1])
     
def RPR_CSurf_OnSelectedChange(trackid,selected):
    """
    Python: Boolean  RPR_CSurf_OnSelectedChange(MediaTrack trackid, Int selected)
    """
    a=_ft['CSurf_OnSelectedChange']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(selected))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_OnSendPanChange(trackid,send_index,pan,relative):
    """
    Python: Float  RPR_CSurf_OnSendPanChange(MediaTrack trackid, Int send_index, Float pan, Boolean relative)
    """
    a=_ft['CSurf_OnSendPanChange']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(send_index),c_double(pan),c_byte(relative))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_CSurf_OnSendVolumeChange(trackid,send_index,volume,relative):
    """
    Python: Float  RPR_CSurf_OnSendVolumeChange(MediaTrack trackid, Int send_index, Float volume, Boolean relative)
    """
    a=_ft['CSurf_OnSendVolumeChange']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(send_index),c_double(volume),c_byte(relative))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_CSurf_OnSoloChange(trackid,solo):
    """
    Python: Boolean  RPR_CSurf_OnSoloChange(MediaTrack trackid, Int solo)
    """
    a=_ft['CSurf_OnSoloChange']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(solo))
    r=f(t[0],t[1])
    return r
     
def RPR_CSurf_OnSoloChangeEx(trackid,solo,allowgang):
    """
    Python: Boolean  RPR_CSurf_OnSoloChangeEx(MediaTrack trackid, Int solo, Boolean allowgang)
    """
    a=_ft['CSurf_OnSoloChangeEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_int(solo),c_byte(allowgang))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CSurf_OnStop():
    """
    Python: RPR_CSurf_OnStop()
    """
    a=_ft['CSurf_OnStop']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_OnTempoChange(bpm):
    """
    Python: RPR_CSurf_OnTempoChange(Float bpm)
    """
    a=_ft['CSurf_OnTempoChange']
    f=CFUNCTYPE(None,c_double)(a)
    t=(c_double(bpm),)
    f(t[0])
     
def RPR_CSurf_OnTrackSelection(trackid):
    """
    Python: RPR_CSurf_OnTrackSelection(MediaTrack trackid)
    """
    a=_ft['CSurf_OnTrackSelection']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',trackid),)
    f(t[0])
     
def RPR_CSurf_OnVolumeChange(trackid,volume,relative):
    """
    Python: Float  RPR_CSurf_OnVolumeChange(MediaTrack trackid, Float volume, Boolean relative)
    """
    a=_ft['CSurf_OnVolumeChange']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(volume),c_byte(relative))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CSurf_OnVolumeChangeEx(trackid,volume,relative,allowGang):
    """
    Python: Float  RPR_CSurf_OnVolumeChangeEx(MediaTrack trackid, Float volume, Boolean relative, Boolean allowGang)
    """
    a=_ft['CSurf_OnVolumeChangeEx']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_byte,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(volume),c_byte(relative),c_byte(allowGang))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_CSurf_OnWidthChange(trackid,width,relative):
    """
    Python: Float  RPR_CSurf_OnWidthChange(MediaTrack trackid, Float width, Boolean relative)
    """
    a=_ft['CSurf_OnWidthChange']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(width),c_byte(relative))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_CSurf_OnWidthChangeEx(trackid,width,relative,allowGang):
    """
    Python: Float  RPR_CSurf_OnWidthChangeEx(MediaTrack trackid, Float width, Boolean relative, Boolean allowGang)
    """
    a=_ft['CSurf_OnWidthChangeEx']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_byte,c_byte)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(width),c_byte(relative),c_byte(allowGang))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_CSurf_OnZoom(xdir,ydir):
    """
    Python: RPR_CSurf_OnZoom(Int xdir, Int ydir)
    """
    a=_ft['CSurf_OnZoom']
    f=CFUNCTYPE(None,c_int,c_int)(a)
    t=(c_int(xdir),c_int(ydir))
    f(t[0],t[1])
     
def RPR_CSurf_ResetAllCachedVolPanStates():
    """
    Python: RPR_CSurf_ResetAllCachedVolPanStates()
    """
    a=_ft['CSurf_ResetAllCachedVolPanStates']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_ScrubAmt(amt):
    """
    Python: RPR_CSurf_ScrubAmt(Float amt)
    """
    a=_ft['CSurf_ScrubAmt']
    f=CFUNCTYPE(None,c_double)(a)
    t=(c_double(amt),)
    f(t[0])
     
def RPR_CSurf_SetAutoMode(mode,ignoresurf):
    """
    Python: RPR_CSurf_SetAutoMode(Int mode, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetAutoMode']
    f=CFUNCTYPE(None,c_int,c_uint64)(a)
    t=(c_int(mode),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1])
     
def RPR_CSurf_SetPlayState(play,pause,rec,ignoresurf):
    """
    Python: RPR_CSurf_SetPlayState(Boolean play, Boolean pause, Boolean rec, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetPlayState']
    f=CFUNCTYPE(None,c_byte,c_byte,c_byte,c_uint64)(a)
    t=(c_byte(play),c_byte(pause),c_byte(rec),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1],t[2],t[3])
     
def RPR_CSurf_SetRepeatState(rep,ignoresurf):
    """
    Python: RPR_CSurf_SetRepeatState(Boolean rep, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetRepeatState']
    f=CFUNCTYPE(None,c_byte,c_uint64)(a)
    t=(c_byte(rep),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1])
     
def RPR_CSurf_SetSurfaceMute(trackid,mute,ignoresurf):
    """
    Python: RPR_CSurf_SetSurfaceMute(MediaTrack trackid, Boolean mute, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetSurfaceMute']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_byte(mute),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1],t[2])
     
def RPR_CSurf_SetSurfacePan(trackid,pan,ignoresurf):
    """
    Python: RPR_CSurf_SetSurfacePan(MediaTrack trackid, Float pan, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetSurfacePan']
    f=CFUNCTYPE(None,c_uint64,c_double,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(pan),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1],t[2])
     
def RPR_CSurf_SetSurfaceRecArm(trackid,recarm,ignoresurf):
    """
    Python: RPR_CSurf_SetSurfaceRecArm(MediaTrack trackid, Boolean recarm, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetSurfaceRecArm']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_byte(recarm),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1],t[2])
     
def RPR_CSurf_SetSurfaceSelected(trackid,selected,ignoresurf):
    """
    Python: RPR_CSurf_SetSurfaceSelected(MediaTrack trackid, Boolean selected, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetSurfaceSelected']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_byte(selected),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1],t[2])
     
def RPR_CSurf_SetSurfaceSolo(trackid,solo,ignoresurf):
    """
    Python: RPR_CSurf_SetSurfaceSolo(MediaTrack trackid, Boolean solo, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetSurfaceSolo']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_byte(solo),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1],t[2])
     
def RPR_CSurf_SetSurfaceVolume(trackid,volume,ignoresurf):
    """
    Python: RPR_CSurf_SetSurfaceVolume(MediaTrack trackid, Float volume, IReaperControlSurface ignoresurf)
    """
    a=_ft['CSurf_SetSurfaceVolume']
    f=CFUNCTYPE(None,c_uint64,c_double,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',trackid),c_double(volume),rpr_packp('IReaperControlSurface*',ignoresurf))
    f(t[0],t[1],t[2])
     
def RPR_CSurf_SetTrackListChange():
    """
    Python: RPR_CSurf_SetTrackListChange()
    """
    a=_ft['CSurf_SetTrackListChange']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_CSurf_TrackFromID(idx,mcpView):
    """
    Python: MediaTrack  RPR_CSurf_TrackFromID(Int idx, Boolean mcpView)
    """
    a=_ft['CSurf_TrackFromID']
    f=CFUNCTYPE(c_uint64,c_int,c_byte)(a)
    t=(c_int(idx),c_byte(mcpView))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_CSurf_TrackToID(track,mcpView):
    """
    Python: Int  RPR_CSurf_TrackToID(MediaTrack track, Boolean mcpView)
    """
    a=_ft['CSurf_TrackToID']
    f=CFUNCTYPE(c_int,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_byte(mcpView))
    r=f(t[0],t[1])
    return r
     
def RPR_DB2SLIDER(x):
    """
    Python: Float  RPR_DB2SLIDER(Float x)
    """
    a=_ft['DB2SLIDER']
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(x),)
    r=f(t[0])
    return r
     
def RPR_DeleteEnvelopePointRange(envelope,time_start,time_end):
    """
    Python: Boolean  RPR_DeleteEnvelopePointRange(TrackEnvelope envelope, Float time_start, Float time_end)
    
    Delete a range of envelope points.
    """
    a=_ft['DeleteEnvelopePointRange']
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_double)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_double(time_start),c_double(time_end))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_DeleteEnvelopePointRangeEx(envelope,autoitem_idx,time_start,time_end):
    """
    Python: Boolean  RPR_DeleteEnvelopePointRangeEx(TrackEnvelope envelope, Int autoitem_idx, Float time_start, Float time_end)
    
    Delete a range of envelope points. autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc.
    """
    a=_ft['DeleteEnvelopePointRangeEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double,c_double)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(autoitem_idx),c_double(time_start),c_double(time_end))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_DeleteExtState(section,key,persist):
    """
    Python: RPR_DeleteExtState(String section, String key, Boolean persist)
    
    Delete the extended state value for a specific section and key. persist=true means the value should remain deleted the next time REAPER is opened. See SetExtState
    , GetExtState
    , HasExtState
    .
    """
    a=_ft['DeleteExtState']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_byte)(a)
    t=(rpr_packsc(section),rpr_packsc(key),c_byte(persist))
    f(t[0],t[1],t[2])
     
def RPR_DeleteProjectMarker(proj,markrgnindexnumber,isrgn):
    """
    Python: Boolean  RPR_DeleteProjectMarker(ReaProject proj, Int markrgnindexnumber, Boolean isrgn)
    
    Delete a marker.  proj==NULL for the active project.
    """
    a=_ft['DeleteProjectMarker']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(markrgnindexnumber),c_byte(isrgn))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_DeleteProjectMarkerByIndex(proj,markrgnidx):
    """
    Python: Boolean  RPR_DeleteProjectMarkerByIndex(ReaProject proj, Int markrgnidx)
    
    Differs from DeleteProjectMarker only in that markrgnidx is 0 for the first marker/region, 1 for the next, etc (see EnumProjectMarkers3
    ), rather than representing the displayed marker/region ID number (see SetProjectMarker4
    ).
    """
    a=_ft['DeleteProjectMarkerByIndex']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(markrgnidx))
    r=f(t[0],t[1])
    return r
     
def RPR_DeleteTakeStretchMarkers(take,idx,countInOptional):
    """
    Python: Int  RPR_DeleteTakeStretchMarkers(MediaItem_Take take, Int idx, const int countInOptional)
    
    Deletes one or more stretch markers. Returns number of stretch markers deleted.
    """
    a=_ft['DeleteTakeStretchMarkers']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(idx),c_int(countInOptional))
    r=f(t[0],t[1],byref(t[2]))
    return (r,take,idx,int(t[2].value))
     
def RPR_DeleteTempoTimeSigMarker(project,markerindex):
    """
    Python: Boolean  RPR_DeleteTempoTimeSigMarker(ReaProject project, Int markerindex)
    
    Delete a tempo/time signature marker.
    """
    a=_ft['DeleteTempoTimeSigMarker']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',project),c_int(markerindex))
    r=f(t[0],t[1])
    return r
     
def RPR_DeleteTrack(tr):
    """
    Python: RPR_DeleteTrack(MediaTrack tr)
    
    deletes a track
    """
    a=_ft['DeleteTrack']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),)
    f(t[0])
     
def RPR_DeleteTrackMediaItem(tr,it):
    """
    Python: Boolean  RPR_DeleteTrackMediaItem(MediaTrack tr, MediaItem it)
    """
    a=_ft['DeleteTrackMediaItem']
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packp('MediaItem*',it))
    r=f(t[0],t[1])
    return r
     
def RPR_DestroyAudioAccessor(accessor):
    """
    Python: RPR_DestroyAudioAccessor(AudioAccessor accessor)
    
    Destroy an audio accessor. Must only call from the main thread. See CreateTakeAudioAccessor
    , CreateTrackAudioAccessor
    , GetAudioAccessorHash
    , GetAudioAccessorStartTime
    , GetAudioAccessorEndTime
    , GetAudioAccessorSamples
    .
    """
    a=_ft['DestroyAudioAccessor']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('AudioAccessor*',accessor),)
    f(t[0])
     
def RPR_Dock_UpdateDockID(ident_str,whichDock):
    """
    Python: RPR_Dock_UpdateDockID(String ident_str, Int whichDock)
    
    updates preference for docker window ident_str to be in dock whichDock on next open
    """
    a=_ft['Dock_UpdateDockID']
    f=CFUNCTYPE(None,c_char_p,c_int)(a)
    t=(rpr_packsc(ident_str),c_int(whichDock))
    f(t[0],t[1])
     
def RPR_DockIsChildOfDock(hwnd,isFloatingDockerOut):
    """
    Python: (Int retval, HWND hwnd, Boolean isFloatingDockerOut) = RPR_DockIsChildOfDock(hwnd, isFloatingDockerOut)
    
    returns dock index that contains hwnd, or -1
    """
    a=_ft['DockIsChildOfDock']
    f=CFUNCTYPE(c_int,c_uint64,c_void_p)(a)
    t=(rpr_packp('HWND',hwnd),c_byte(isFloatingDockerOut))
    r=f(t[0],byref(t[1]))
    return (r,hwnd,int(t[1].value))
     
def RPR_DockWindowActivate(hwnd):
    """
    Python: RPR_DockWindowActivate(HWND hwnd)
    """
    a=_ft['DockWindowActivate']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('HWND',hwnd),)
    f(t[0])
     
def RPR_DockWindowAdd(hwnd,name,pos,allowShow):
    """
    Python: RPR_DockWindowAdd(HWND hwnd, String name, Int pos, Boolean allowShow)
    """
    a=_ft['DockWindowAdd']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int,c_byte)(a)
    t=(rpr_packp('HWND',hwnd),rpr_packsc(name),c_int(pos),c_byte(allowShow))
    f(t[0],t[1],t[2],t[3])
     
def RPR_DockWindowAddEx(hwnd,name,identstr,allowShow):
    """
    Python: RPR_DockWindowAddEx(HWND hwnd, String name, String identstr, Boolean allowShow)
    """
    a=_ft['DockWindowAddEx']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_char_p,c_byte)(a)
    t=(rpr_packp('HWND',hwnd),rpr_packsc(name),rpr_packsc(identstr),c_byte(allowShow))
    f(t[0],t[1],t[2],t[3])
     
def RPR_DockWindowRefresh():
    """
    Python: RPR_DockWindowRefresh()
    """
    a=_ft['DockWindowRefresh']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_DockWindowRefreshForHWND(hwnd):
    """
    Python: RPR_DockWindowRefreshForHWND(HWND hwnd)
    """
    a=_ft['DockWindowRefreshForHWND']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('HWND',hwnd),)
    f(t[0])
     
def RPR_DockWindowRemove(hwnd):
    """
    Python: RPR_DockWindowRemove(HWND hwnd)
    """
    a=_ft['DockWindowRemove']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('HWND',hwnd),)
    f(t[0])
     
def RPR_EditTempoTimeSigMarker(project,markerindex):
    """
    Python: Boolean  RPR_EditTempoTimeSigMarker(ReaProject project, Int markerindex)
    
    Open the tempo/time signature marker editor dialog.
    """
    a=_ft['EditTempoTimeSigMarker']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',project),c_int(markerindex))
    r=f(t[0],t[1])
    return r
     
def RPR_EnsureNotCompletelyOffscreen(rInOut):
    """
    Python: RPR_EnsureNotCompletelyOffscreen(RECT rInOut)
    
    call with a saved window rect for your window and it'll correct any positioning info.
    """
    a=_ft['EnsureNotCompletelyOffscreen']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('RECT*',rInOut),)
    f(t[0])
     
def RPR_EnumerateFiles(path,fileindex):
    """
    Python: String  RPR_EnumerateFiles(String path, Int fileindex)
    
    List the files in the "path" directory. Returns NULL (or empty string, in Lua) when all files have been listed. See EnumerateSubdirectories
    """
    a=_ft['EnumerateFiles']
    f=CFUNCTYPE(c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(path),c_int(fileindex))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_EnumerateSubdirectories(path,subdirindex):
    """
    Python: String  RPR_EnumerateSubdirectories(String path, Int subdirindex)
    
    List the subdirectories in the "path" directory. Returns NULL (or empty string, in Lua) when all subdirectories have been listed. See EnumerateFiles
    """
    a=_ft['EnumerateSubdirectories']
    f=CFUNCTYPE(c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(path),c_int(subdirindex))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_EnumPitchShiftModes(mode,strOut):
    """
    Python: Boolean  RPR_EnumPitchShiftModes(Int mode, String strOut)
    
    Start querying modes at 0, returns FALSE when no more modes possible, sets strOut to NULL if a mode is currently unsupported
    """
    a=_ft['EnumPitchShiftModes']
    f=CFUNCTYPE(c_byte,c_int,c_uint64)(a)
    t=(c_int(mode),rpr_packp('char**',strOut))
    r=f(t[0],t[1])
    return r
     
def RPR_EnumPitchShiftSubModes(mode,submode):
    """
    Python: String  RPR_EnumPitchShiftSubModes(Int mode, Int submode)
    
    Returns submode name, or NULL
    """
    a=_ft['EnumPitchShiftSubModes']
    f=CFUNCTYPE(c_char_p,c_int,c_int)(a)
    t=(c_int(mode),c_int(submode))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_EnumProjectMarkers(idx,isrgnOut,posOut,rgnendOut,nameOut,markrgnindexnumberOut):
    """
    Python: (Int retval, Int idx, Boolean isrgnOut, Float posOut, Float rgnendOut, String nameOut, Int markrgnindexnumberOut) = RPR_EnumProjectMarkers(idx, isrgnOut, posOut, rgnendOut, nameOut, markrgnindexnumberOut)
    """
    a=_ft['EnumProjectMarkers']
    f=CFUNCTYPE(c_int,c_int,c_void_p,c_void_p,c_void_p,c_uint64,c_void_p)(a)
    t=(c_int(idx),c_byte(isrgnOut),c_double(posOut),c_double(rgnendOut),rpr_packp('char**',nameOut),c_int(markrgnindexnumberOut))
    r=f(t[0],byref(t[1]),byref(t[2]),byref(t[3]),t[4],byref(t[5]))
    return (r,idx,int(t[1].value),float(t[2].value),float(t[3].value),nameOut,int(t[5].value))
     
def RPR_EnumProjectMarkers2(proj,idx,isrgnOut,posOut,rgnendOut,nameOut,markrgnindexnumberOut):
    """
    Python: (Int retval, ReaProject proj, Int idx, Boolean isrgnOut, Float posOut, Float rgnendOut, String nameOut, Int markrgnindexnumberOut) = RPR_EnumProjectMarkers2(proj, idx, isrgnOut, posOut, rgnendOut, nameOut, markrgnindexnumberOut)
    """
    a=_ft['EnumProjectMarkers2']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_uint64,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(idx),c_byte(isrgnOut),c_double(posOut),c_double(rgnendOut),rpr_packp('char**',nameOut),c_int(markrgnindexnumberOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),t[5],byref(t[6]))
    return (r,proj,idx,int(t[2].value),float(t[3].value),float(t[4].value),nameOut,int(t[6].value))
     
def RPR_EnumProjectMarkers3(proj,idx,isrgnOut,posOut,rgnendOut,nameOut,markrgnindexnumberOut,colorOut):
    """
    Python: (Int retval, ReaProject proj, Int idx, Boolean isrgnOut, Float posOut, Float rgnendOut, String nameOut, Int markrgnindexnumberOut, Int colorOut) = RPR_EnumProjectMarkers3(proj, idx, isrgnOut, posOut, rgnendOut, nameOut, markrgnindexnumberOut, colorOut)
    """
    a=_ft['EnumProjectMarkers3']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(idx),c_byte(isrgnOut),c_double(posOut),c_double(rgnendOut),rpr_packp('char**',nameOut),c_int(markrgnindexnumberOut),c_int(colorOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),t[5],byref(t[6]),byref(t[7]))
    return (r,proj,idx,int(t[2].value),float(t[3].value),float(t[4].value),nameOut,int(t[6].value),int(t[7].value))
     
def RPR_EnumProjects(idx,projfn,projfn_sz):
    """
    Python: (ReaProject retval, Int idx, String projfn, Int projfn_sz) = RPR_EnumProjects(idx, projfn, projfn_sz)
    
    idx=-1 for current project,projfn can be NULL if not interested in filename. use idx 0x40000000 for currently rendering project, if any.
    """
    a=_ft['EnumProjects']
    f=CFUNCTYPE(c_uint64,c_int,c_char_p,c_int)(a)
    t=(c_int(idx),rpr_packs(projfn),c_int(projfn_sz))
    r=f(t[0],t[1],t[2])
    return (rpr_unpackp('ReaProject*',r),idx,rpr_unpacks(t[1]),projfn_sz)
     
def RPR_EnumProjExtState(proj,extname,idx,keyOutOptional,keyOutOptional_sz,valOutOptional,valOutOptional_sz):
    """
    Python: (Boolean retval, ReaProject proj, String extname, Int idx, String keyOutOptional, Int keyOutOptional_sz, String valOutOptional, Int valOutOptional_sz) = RPR_EnumProjExtState(proj, extname, idx, keyOutOptional, keyOutOptional_sz, valOutOptional, valOutOptional_sz)
    
    Enumerate the data stored with the project for a specific extname. Returns false when there is no more data. See SetProjExtState
    , GetProjExtState
    .
    """
    a=_ft['EnumProjExtState']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_char_p,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(extname),c_int(idx),rpr_packs(keyOutOptional),c_int(keyOutOptional_sz),rpr_packs(valOutOptional),c_int(valOutOptional_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return (r,proj,extname,idx,rpr_unpacks(t[3]),keyOutOptional_sz,rpr_unpacks(t[5]),valOutOptional_sz)
     
def RPR_EnumRegionRenderMatrix(proj,regionindex,rendertrack):
    """
    Python: MediaTrack  RPR_EnumRegionRenderMatrix(ReaProject proj, Int regionindex, Int rendertrack)
    
    Enumerate which tracks will be rendered within this region when using the region render matrix. When called with rendertrack==0, the function returns the first track that will be rendered (which may be the master track); rendertrack==1 will return the next track rendered, and so on. The function returns NULL when there are no more tracks that will be rendered within this region.
    """
    a=_ft['EnumRegionRenderMatrix']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(regionindex),c_int(rendertrack))
    r=f(t[0],t[1],t[2])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_EnumTrackMIDIProgramNames(track,programNumber,programName,programName_sz):
    """
    Python: (Boolean retval, Int track, Int programNumber, String programName, Int programName_sz) = RPR_EnumTrackMIDIProgramNames(track, programNumber, programName, programName_sz)
    
    returns false if there are no plugins on the track that support MIDI programs,or if all programs have been enumerated
    """
    a=_ft['EnumTrackMIDIProgramNames']
    f=CFUNCTYPE(c_byte,c_int,c_int,c_char_p,c_int)(a)
    t=(c_int(track),c_int(programNumber),rpr_packs(programName),c_int(programName_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,programNumber,rpr_unpacks(t[2]),programName_sz)
     
def RPR_EnumTrackMIDIProgramNamesEx(proj,track,programNumber,programName,programName_sz):
    """
    Python: (Boolean retval, ReaProject proj, MediaTrack track, Int programNumber, String programName, Int programName_sz) = RPR_EnumTrackMIDIProgramNamesEx(proj, track, programNumber, programName, programName_sz)
    
    returns false if there are no plugins on the track that support MIDI programs,or if all programs have been enumerated
    """
    a=_ft['EnumTrackMIDIProgramNamesEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packp('MediaTrack*',track),c_int(programNumber),rpr_packs(programName),c_int(programName_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,proj,track,programNumber,rpr_unpacks(t[3]),programName_sz)
     
def RPR_Envelope_Evaluate(envelope,time,samplerate,samplesRequested,valueOutOptional,dVdSOutOptional,ddVdSOutOptional,dddVdSOutOptional):
    """
    Python: (Int retval, TrackEnvelope envelope, Float time, Float samplerate, Int samplesRequested, Float valueOutOptional, Float dVdSOutOptional, Float ddVdSOutOptional, Float dddVdSOutOptional) = RPR_Envelope_Evaluate(envelope, time, samplerate, samplesRequested, valueOutOptional, dVdSOutOptional, ddVdSOutOptional, dddVdSOutOptional)
    
    Get the effective envelope value at a given time position. samplesRequested is how long the caller expects until the next call to Envelope_Evaluate (often, the buffer block size). The return value is how many samples beyond that time position that the returned values are valid. dVdS is the change in value per sample (first derivative), ddVdS is the seond derivative, dddVdS is the third derivative. See GetEnvelopeScalingMode
    .
    """
    a=_ft['Envelope_Evaluate']
    f=CFUNCTYPE(c_int,c_uint64,c_double,c_double,c_int,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_double(time),c_double(samplerate),c_int(samplesRequested),c_double(valueOutOptional),c_double(dVdSOutOptional),c_double(ddVdSOutOptional),c_double(dddVdSOutOptional))
    r=f(t[0],t[1],t[2],t[3],byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]))
    return (r,envelope,time,samplerate,samplesRequested,float(t[4].value),float(t[5].value),float(t[6].value),float(t[7].value))
     
def RPR_Envelope_FormatValue(env,value,bufOut,bufOut_sz):
    """
    Python: (TrackEnvelope env, Float value, String bufOut, Int bufOut_sz) = RPR_Envelope_FormatValue(env, value, bufOut, bufOut_sz)
    
    Formats the value of an envelope to a user-readable form
    """
    a=_ft['Envelope_FormatValue']
    f=CFUNCTYPE(None,c_uint64,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('TrackEnvelope*',env),c_double(value),rpr_packs(bufOut),c_int(bufOut_sz))
    f(t[0],t[1],t[2],t[3])
    return (env,value,rpr_unpacks(t[2]),bufOut_sz)
     
def RPR_Envelope_GetParentTake(env,indexOutOptional,index2OutOptional):
    """
    Python: (MediaItem_Take retval, TrackEnvelope env, Int indexOutOptional, Int index2OutOptional) = RPR_Envelope_GetParentTake(env, indexOutOptional, index2OutOptional)
    
    If take envelope, gets the take from the envelope. If FX, indexOutOptional set to FX index, index2OutOptional set to parameter index, otherwise -1.
    """
    a=_ft['Envelope_GetParentTake']
    f=CFUNCTYPE(c_uint64,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',env),c_int(indexOutOptional),c_int(index2OutOptional))
    r=f(t[0],byref(t[1]),byref(t[2]))
    return (rpr_unpackp('MediaItem_Take*',r),env,int(t[1].value),int(t[2].value))
     
def RPR_Envelope_GetParentTrack(env,indexOutOptional,index2OutOptional):
    """
    Python: (MediaTrack retval, TrackEnvelope env, Int indexOutOptional, Int index2OutOptional) = RPR_Envelope_GetParentTrack(env, indexOutOptional, index2OutOptional)
    
    If track envelope, gets the track from the envelope. If FX, indexOutOptional set to FX index, index2OutOptional set to parameter index, otherwise -1.
    """
    a=_ft['Envelope_GetParentTrack']
    f=CFUNCTYPE(c_uint64,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',env),c_int(indexOutOptional),c_int(index2OutOptional))
    r=f(t[0],byref(t[1]),byref(t[2]))
    return (rpr_unpackp('MediaTrack*',r),env,int(t[1].value),int(t[2].value))
     
def RPR_Envelope_SortPoints(envelope):
    """
    Python: Boolean  RPR_Envelope_SortPoints(TrackEnvelope envelope)
    
    Sort envelope points by time. See SetEnvelopePoint
    , InsertEnvelopePoint
    .
    """
    a=_ft['Envelope_SortPoints']
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),)
    r=f(t[0])
    return r
     
def RPR_Envelope_SortPointsEx(envelope,autoitem_idx):
    """
    Python: Boolean  RPR_Envelope_SortPointsEx(TrackEnvelope envelope, Int autoitem_idx)
    
    Sort envelope points by time.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See SetEnvelopePoint
    , InsertEnvelopePoint
    .
    """
    a=_ft['Envelope_SortPointsEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(autoitem_idx))
    r=f(t[0],t[1])
    return r
     
def RPR_ExecProcess(cmdline,timeoutmsec):
    """
    Python: String  RPR_ExecProcess(String cmdline, Int timeoutmsec)
    
    Executes command line, returns NULL on total failure, otherwise the return value, a newline, and then the output of the command. If timeoutmsec is 0, command will be allowed to run indefinitely (recommended for large amounts of returned output). timeoutmsec is -1 for no wait/terminate, -2 for no wait and minimize
    """
    a=_ft['ExecProcess']
    f=CFUNCTYPE(c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(cmdline),c_int(timeoutmsec))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_file_exists(path):
    """
    Python: Boolean  RPR_file_exists(String path)
    
    returns true if path points to a valid, readable file
    """
    a=_ft['file_exists']
    f=CFUNCTYPE(c_byte,c_char_p)(a)
    t=(rpr_packsc(path),)
    r=f(t[0])
    return r
     
def RPR_FindTempoTimeSigMarker(project,time):
    """
    Python: Int  RPR_FindTempoTimeSigMarker(ReaProject project, Float time)
    
    Find the tempo/time signature marker that falls at or before this time position (the marker that is in effect as of this time position).
    """
    a=_ft['FindTempoTimeSigMarker']
    f=CFUNCTYPE(c_int,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',project),c_double(time))
    r=f(t[0],t[1])
    return r
     
def RPR_format_timestr(tpos,buf,buf_sz):
    """
    Python: (Float tpos, String buf, Int buf_sz) = RPR_format_timestr(tpos, buf, buf_sz)
    
    Format tpos (which is time in seconds) as hh:mm:ss.sss. See format_timestr_pos
    , format_timestr_len
    .
    """
    a=_ft['format_timestr']
    f=CFUNCTYPE(None,c_double,c_char_p,c_int)(a)
    t=(c_double(tpos),rpr_packs(buf),c_int(buf_sz))
    f(t[0],t[1],t[2])
    return (tpos,rpr_unpacks(t[1]),buf_sz)
     
def RPR_format_timestr_len(tpos,buf,buf_sz,offset,modeoverride):
    """
    Python: (Float tpos, String buf, Int buf_sz, Float offset, Int modeoverride) = RPR_format_timestr_len(tpos, buf, buf_sz, offset, modeoverride)
    
    time formatting mode overrides: -1=proj default.
    
    0=time
    
    1=measures.beats + time
    
    2=measures.beats
    
    3=seconds
    
    4=samples
    
    5=h:m:s:f
    
    offset is start of where the length will be calculated from
    """
    a=_ft['format_timestr_len']
    f=CFUNCTYPE(None,c_double,c_char_p,c_int,c_double,c_int)(a)
    t=(c_double(tpos),rpr_packs(buf),c_int(buf_sz),c_double(offset),c_int(modeoverride))
    f(t[0],t[1],t[2],t[3],t[4])
    return (tpos,rpr_unpacks(t[1]),buf_sz,offset,modeoverride)
     
def RPR_format_timestr_pos(tpos,buf,buf_sz,modeoverride):
    """
    Python: (Float tpos, String buf, Int buf_sz, Int modeoverride) = RPR_format_timestr_pos(tpos, buf, buf_sz, modeoverride)
    
    time formatting mode overrides: -1=proj default.
    
    0=time
    
    1=measures.beats + time
    
    2=measures.beats
    
    3=seconds
    
    4=samples
    
    5=h:m:s:f
    """
    a=_ft['format_timestr_pos']
    f=CFUNCTYPE(None,c_double,c_char_p,c_int,c_int)(a)
    t=(c_double(tpos),rpr_packs(buf),c_int(buf_sz),c_int(modeoverride))
    f(t[0],t[1],t[2],t[3])
    return (tpos,rpr_unpacks(t[1]),buf_sz,modeoverride)
     
def RPR_genGuid(g):
    """
    Python: RPR_genGuid(GUID g)
    """
    a=_ft['genGuid']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('GUID*',g),)
    f(t[0])
     
def RPR_get_ini_file():
    """
    Python: String  RPR_get_ini_file()
    
    Get reaper.ini full filename.
    """
    a=_ft['get_ini_file']
    f=CFUNCTYPE(c_char_p)(a)
    r=f()
    return str(r.decode())
     
def RPR_GetActiveTake(item):
    """
    Python: MediaItem_Take  RPR_GetActiveTake(MediaItem item)
    
    get the active take in this item
    """
    a=_ft['GetActiveTake']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return rpr_unpackp('MediaItem_Take*',r)
     
def RPR_GetAllProjectPlayStates(ignoreProject):
    """
    Python: Int  RPR_GetAllProjectPlayStates(ReaProject ignoreProject)
    
    returns the bitwise OR of all project play states (1=playing, 2=pause, 4=recording)
    """
    a=_ft['GetAllProjectPlayStates']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',ignoreProject),)
    r=f(t[0])
    return r
     
def RPR_GetAppVersion():
    """
    Python: String  RPR_GetAppVersion()
    """
    a=_ft['GetAppVersion']
    f=CFUNCTYPE(c_char_p)(a)
    r=f()
    return str(r.decode())
     
def RPR_GetArmedCommand(secOut,secOut_sz):
    """
    Python: (Int retval, String secOut, Int secOut_sz) = RPR_GetArmedCommand(secOut, secOut_sz)
    
    gets the currently armed command and section name (returns 0 if nothing armed). section name is empty-string for main section.
    """
    a=_ft['GetArmedCommand']
    f=CFUNCTYPE(c_int,c_char_p,c_int)(a)
    t=(rpr_packs(secOut),c_int(secOut_sz))
    r=f(t[0],t[1])
    return (r,rpr_unpacks(t[0]),secOut_sz)
     
def RPR_GetAudioAccessorEndTime(accessor):
    """
    Python: Float  RPR_GetAudioAccessorEndTime(AudioAccessor accessor)
    
    Get the end time of the audio that can be returned from this accessor. See CreateTakeAudioAccessor
    , CreateTrackAudioAccessor
    , DestroyAudioAccessor
    , GetAudioAccessorHash
    , GetAudioAccessorStartTime
    , GetAudioAccessorSamples
    .
    """
    a=_ft['GetAudioAccessorEndTime']
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('AudioAccessor*',accessor),)
    r=f(t[0])
    return r
     
def RPR_GetAudioAccessorHash(accessor,hashNeed128):
    """
    Python: (AudioAccessor accessor, String hashNeed128) = RPR_GetAudioAccessorHash(accessor, hashNeed128)
    
    Get a short hash string (128 chars or less) that will change only if the underlying samples change.  See CreateTakeAudioAccessor
    , CreateTrackAudioAccessor
    , DestroyAudioAccessor
    , GetAudioAccessorStartTime
    , GetAudioAccessorEndTime
    , GetAudioAccessorSamples
    .
    """
    a=_ft['GetAudioAccessorHash']
    f=CFUNCTYPE(None,c_uint64,c_char_p)(a)
    t=(rpr_packp('AudioAccessor*',accessor),rpr_packs(hashNeed128))
    f(t[0],t[1])
    return (accessor,rpr_unpacks(t[1]))
     
def RPR_GetAudioAccessorStartTime(accessor):
    """
    Python: Float  RPR_GetAudioAccessorStartTime(AudioAccessor accessor)
    
    Get the start time of the audio that can be returned from this accessor. See CreateTakeAudioAccessor
    , CreateTrackAudioAccessor
    , DestroyAudioAccessor
    , GetAudioAccessorHash
    , GetAudioAccessorEndTime
    , GetAudioAccessorSamples
    .
    """
    a=_ft['GetAudioAccessorStartTime']
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('AudioAccessor*',accessor),)
    r=f(t[0])
    return r
     
def RPR_GetConfigWantsDock(ident_str):
    """
    Python: Int  RPR_GetConfigWantsDock(String ident_str)
    
    gets the dock ID desired by ident_str, if any
    """
    a=_ft['GetConfigWantsDock']
    f=CFUNCTYPE(c_int,c_char_p)(a)
    t=(rpr_packsc(ident_str),)
    r=f(t[0])
    return r
     
def RPR_GetCurrentProjectInLoadSave():
    """
    Python: ReaProject  RPR_GetCurrentProjectInLoadSave()
    
    returns current project if in load/save (usually only used from project_config_extension_t)
    """
    a=_ft['GetCurrentProjectInLoadSave']
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('ReaProject*',r)
     
def RPR_GetCursorContext():
    """
    Python: Int  RPR_GetCursorContext()
    
    return the current cursor context: 0 if track panels, 1 if items, 2 if envelopes, otherwise unknown
    """
    a=_ft['GetCursorContext']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetCursorContext2(want_last_valid):
    """
    Python: Int  RPR_GetCursorContext2(Boolean want_last_valid)
    
    0 if track panels, 1 if items, 2 if envelopes, otherwise unknown (unlikely when want_last_valid is true)
    """
    a=_ft['GetCursorContext2']
    f=CFUNCTYPE(c_int,c_byte)(a)
    t=(c_byte(want_last_valid),)
    r=f(t[0])
    return r
     
def RPR_GetCursorPosition():
    """
    Python: Float  RPR_GetCursorPosition()
    
    edit cursor position
    """
    a=_ft['GetCursorPosition']
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def RPR_GetCursorPositionEx(proj):
    """
    Python: Float  RPR_GetCursorPositionEx(ReaProject proj)
    
    edit cursor position
    """
    a=_ft['GetCursorPositionEx']
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_GetDisplayedMediaItemColor(item):
    """
    Python: Int  RPR_GetDisplayedMediaItemColor(MediaItem item)
    
    see GetDisplayedMediaItemColor2
    .
    """
    a=_ft['GetDisplayedMediaItemColor']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def RPR_GetDisplayedMediaItemColor2(item,take):
    """
    Python: Int  RPR_GetDisplayedMediaItemColor2(MediaItem item, MediaItem_Take take)
    
    Returns the custom take, item, or track color that is used (according to the user preference) to color the media item. The returned color is OS dependent|0x01000000 (i.e. ColorToNative(r,g,b)|0x01000000), so a return of zero means "no color", not black.
    """
    a=_ft['GetDisplayedMediaItemColor2']
    f=CFUNCTYPE(c_int,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packp('MediaItem_Take*',take))
    r=f(t[0],t[1])
    return r
     
def RPR_GetEnvelopeName(env,buf,buf_sz):
    """
    Python: (Boolean retval, TrackEnvelope env, String buf, Int buf_sz) = RPR_GetEnvelopeName(env, buf, buf_sz)
    """
    a=_ft['GetEnvelopeName']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('TrackEnvelope*',env),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2])
    return (r,env,rpr_unpacks(t[1]),buf_sz)
     
def RPR_GetEnvelopePoint(envelope,ptidx,timeOutOptional,valueOutOptional,shapeOutOptional,tensionOutOptional,selectedOutOptional):
    """
    Python: (Boolean retval, TrackEnvelope envelope, Int ptidx, Float timeOutOptional, Float valueOutOptional, Int shapeOutOptional, Float tensionOutOptional, Boolean selectedOutOptional) = RPR_GetEnvelopePoint(envelope, ptidx, timeOutOptional, valueOutOptional, shapeOutOptional, tensionOutOptional, selectedOutOptional)
    
    Get the attributes of an envelope point. See GetEnvelopePointByTime
    , SetEnvelopePoint
    .
    """
    a=_ft['GetEnvelopePoint']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(ptidx),c_double(timeOutOptional),c_double(valueOutOptional),c_int(shapeOutOptional),c_double(tensionOutOptional),c_byte(selectedOutOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]))
    return (r,envelope,ptidx,float(t[2].value),float(t[3].value),int(t[4].value),float(t[5].value),int(t[6].value))
     
def RPR_GetEnvelopePointByTime(envelope,time):
    """
    Python: Int  RPR_GetEnvelopePointByTime(TrackEnvelope envelope, Float time)
    
    Returns the envelope point at or immediately prior to the given time position. See GetEnvelopePoint
    , SetEnvelopePoint
    , Envelope_Evaluate
    .
    """
    a=_ft['GetEnvelopePointByTime']
    f=CFUNCTYPE(c_int,c_uint64,c_double)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_double(time))
    r=f(t[0],t[1])
    return r
     
def RPR_GetEnvelopePointByTimeEx(envelope,autoitem_idx,time):
    """
    Python: Int  RPR_GetEnvelopePointByTimeEx(TrackEnvelope envelope, Int autoitem_idx, Float time)
    
    Returns the envelope point at or immediately prior to the given time position.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePoint
    , SetEnvelopePoint
    , Envelope_Evaluate
    .
    """
    a=_ft['GetEnvelopePointByTimeEx']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_double)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(autoitem_idx),c_double(time))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_GetEnvelopePointEx(envelope,autoitem_idx,ptidx,timeOutOptional,valueOutOptional,shapeOutOptional,tensionOutOptional,selectedOutOptional):
    """
    Python: (Boolean retval, TrackEnvelope envelope, Int autoitem_idx, Int ptidx, Float timeOutOptional, Float valueOutOptional, Int shapeOutOptional, Float tensionOutOptional, Boolean selectedOutOptional) = RPR_GetEnvelopePointEx(envelope, autoitem_idx, ptidx, timeOutOptional, valueOutOptional, shapeOutOptional, tensionOutOptional, selectedOutOptional)
    
    Get the attributes of an envelope point.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePointByTime
    , SetEnvelopePoint
    .
    """
    a=_ft['GetEnvelopePointEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(autoitem_idx),c_int(ptidx),c_double(timeOutOptional),c_double(valueOutOptional),c_int(shapeOutOptional),c_double(tensionOutOptional),c_byte(selectedOutOptional))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]))
    return (r,envelope,autoitem_idx,ptidx,float(t[3].value),float(t[4].value),int(t[5].value),float(t[6].value),int(t[7].value))
     
def RPR_GetEnvelopeScalingMode(env):
    """
    Python: Int  RPR_GetEnvelopeScalingMode(TrackEnvelope env)
    
    Returns the envelope scaling mode: 0=no scaling, 1=fader scaling. All API functions deal with raw envelope point values, to convert raw from/to scaled values see ScaleFromEnvelopeMode
    , ScaleToEnvelopeMode
    .
    """
    a=_ft['GetEnvelopeScalingMode']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('TrackEnvelope*',env),)
    r=f(t[0])
    return r
     
def RPR_GetEnvelopeStateChunk(env,strNeedBig,strNeedBig_sz,isundoOptional):
    """
    Python: (Boolean retval, TrackEnvelope env, String strNeedBig, Int strNeedBig_sz, Boolean isundoOptional) = RPR_GetEnvelopeStateChunk(env, strNeedBig, strNeedBig_sz, isundoOptional)
    
    Gets the RPPXML state of an envelope, returns true if successful. Undo flag is a performance/caching hint.
    """
    a=_ft['GetEnvelopeStateChunk']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_byte)(a)
    t=(rpr_packp('TrackEnvelope*',env),rpr_packs(strNeedBig),c_int(strNeedBig_sz),c_byte(isundoOptional))
    r=f(t[0],t[1],t[2],t[3])
    return (r,env,rpr_unpacks(t[1]),strNeedBig_sz,isundoOptional)
     
def RPR_GetExePath():
    """
    Python: String  RPR_GetExePath()
    
    returns path of REAPER.exe (not including EXE), i.e. C:\Program Files\REAPER
    """
    a=_ft['GetExePath']
    f=CFUNCTYPE(c_char_p)(a)
    r=f()
    return str(r.decode())
     
def RPR_GetExtState(section,key):
    """
    Python: String  RPR_GetExtState(String section, String key)
    
    Get the extended state value for a specific section and key. See SetExtState
    , DeleteExtState
    , HasExtState
    .
    """
    a=_ft['GetExtState']
    f=CFUNCTYPE(c_char_p,c_char_p,c_char_p)(a)
    t=(rpr_packsc(section),rpr_packsc(key))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_GetFocusedFX(tracknumberOut,itemnumberOut,fxnumberOut):
    """
    Python: (Int retval, Int tracknumberOut, Int itemnumberOut, Int fxnumberOut) = RPR_GetFocusedFX(tracknumberOut, itemnumberOut, fxnumberOut)
    
    Returns 1 if a track FX window has focus, 2 if an item FX window has focus, 0 if no FX window has focus. tracknumber==0 means the master track, 1 means track 1, etc. itemnumber and fxnumber are zero-based. If item FX, fxnumber will have the high word be the take index, the low word the FX index. See GetLastTouchedFX
    .
    """
    a=_ft['GetFocusedFX']
    f=CFUNCTYPE(c_int,c_void_p,c_void_p,c_void_p)(a)
    t=(c_int(tracknumberOut),c_int(itemnumberOut),c_int(fxnumberOut))
    r=f(byref(t[0]),byref(t[1]),byref(t[2]))
    return (r,int(t[0].value),int(t[1].value),int(t[2].value))
     
def RPR_GetFreeDiskSpaceForRecordPath(proj,pathidx):
    """
    Python: Int  RPR_GetFreeDiskSpaceForRecordPath(ReaProject proj, Int pathidx)
    
    returns free disk space in megabytes, pathIdx 0 for normal, 1 for alternate.
    """
    a=_ft['GetFreeDiskSpaceForRecordPath']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(pathidx))
    r=f(t[0],t[1])
    return r
     
def RPR_GetFXEnvelope(track,fxindex,parameterindex,create):
    """
    Python: TrackEnvelope  RPR_GetFXEnvelope(MediaTrack track, Int fxindex, Int parameterindex, Boolean create)
    
    Returns the FX parameter envelope. If the envelope does not exist and create=true, the envelope will be created.
    """
    a=_ft['GetFXEnvelope']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fxindex),c_int(parameterindex),c_byte(create))
    r=f(t[0],t[1],t[2],t[3])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetGlobalAutomationOverride():
    """
    Python: Int  RPR_GetGlobalAutomationOverride()
    
    return -1=no override, 0=trim/read, 1=read, 2=touch, 3=write, 4=latch, 5=bypass
    """
    a=_ft['GetGlobalAutomationOverride']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetHZoomLevel():
    """
    Python: Float  RPR_GetHZoomLevel()
    
    returns pixels/second
    """
    a=_ft['GetHZoomLevel']
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def RPR_GetInputChannelName(channelIndex):
    """
    Python: String  RPR_GetInputChannelName(Int channelIndex)
    """
    a=_ft['GetInputChannelName']
    f=CFUNCTYPE(c_char_p,c_int)(a)
    t=(c_int(channelIndex),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_GetInputOutputLatency(inputlatencyOut,outputLatencyOut):
    """
    Python: (Int inputlatencyOut, Int outputLatencyOut) = RPR_GetInputOutputLatency(inputlatencyOut, outputLatencyOut)
    
    Gets the audio device input/output latency in samples
    """
    a=_ft['GetInputOutputLatency']
    f=CFUNCTYPE(None,c_void_p,c_void_p)(a)
    t=(c_int(inputlatencyOut),c_int(outputLatencyOut))
    f(byref(t[0]),byref(t[1]))
    return (int(t[0].value),int(t[1].value))
     
def RPR_GetItemEditingTime2(which_itemOut,flagsOut):
    """
    Python: (Float retval, PCM_source* which_itemOut, Int flagsOut) = RPR_GetItemEditingTime2(which_itemOut, flagsOut)
    
    returns time of relevant edit, set which_item to the pcm_source (if applicable), flags (if specified) will be set to 1 for edge resizing, 2 for fade change, 4 for item move
    """
    a=_ft['GetItemEditingTime2']
    f=CFUNCTYPE(c_double,c_uint64,c_void_p)(a)
    t=(rpr_packp('PCM_source**',which_itemOut),c_int(flagsOut))
    r=f(t[0],byref(t[1]))
    return (r,which_itemOut,int(t[1].value))
     
def RPR_GetItemProjectContext(item):
    """
    Python: ReaProject  RPR_GetItemProjectContext(MediaItem item)
    """
    a=_ft['GetItemProjectContext']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return rpr_unpackp('ReaProject*',r)
     
def RPR_GetItemStateChunk(item,strNeedBig,strNeedBig_sz,isundoOptional):
    """
    Python: (Boolean retval, MediaItem item, String strNeedBig, Int strNeedBig_sz, Boolean isundoOptional) = RPR_GetItemStateChunk(item, strNeedBig, strNeedBig_sz, isundoOptional)
    
    Gets the RPPXML state of an item, returns true if successful. Undo flag is a performance/caching hint.
    """
    a=_ft['GetItemStateChunk']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packs(strNeedBig),c_int(strNeedBig_sz),c_byte(isundoOptional))
    r=f(t[0],t[1],t[2],t[3])
    return (r,item,rpr_unpacks(t[1]),strNeedBig_sz,isundoOptional)
     
def RPR_GetLastColorThemeFile():
    """
    Python: String  RPR_GetLastColorThemeFile()
    """
    a=_ft['GetLastColorThemeFile']
    f=CFUNCTYPE(c_char_p)(a)
    r=f()
    return str(r.decode())
     
def RPR_GetLastMarkerAndCurRegion(proj,time,markeridxOut,regionidxOut):
    """
    Python: (ReaProject proj, Float time, Int markeridxOut, Int regionidxOut) = RPR_GetLastMarkerAndCurRegion(proj, time, markeridxOut, regionidxOut)
    
    Get the last project marker before time, and/or the project region that includes time. markeridx and regionidx are returned not necessarily as the displayed marker/region index, but as the index that can be passed to EnumProjectMarkers. Either or both of markeridx and regionidx may be NULL. See EnumProjectMarkers
    .
    """
    a=_ft['GetLastMarkerAndCurRegion']
    f=CFUNCTYPE(None,c_uint64,c_double,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(time),c_int(markeridxOut),c_int(regionidxOut))
    f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (proj,time,int(t[2].value),int(t[3].value))
     
def RPR_GetLastTouchedFX(tracknumberOut,fxnumberOut,paramnumberOut):
    """
    Python: (Boolean retval, Int tracknumberOut, Int fxnumberOut, Int paramnumberOut) = RPR_GetLastTouchedFX(tracknumberOut, fxnumberOut, paramnumberOut)
    
    Returns true if the last touched FX parameter is valid, false otherwise. tracknumber==0 means the master track, 1 means track 1, etc. fxnumber and paramnumber are zero-based. See GetFocusedFX
    .
    """
    a=_ft['GetLastTouchedFX']
    f=CFUNCTYPE(c_byte,c_void_p,c_void_p,c_void_p)(a)
    t=(c_int(tracknumberOut),c_int(fxnumberOut),c_int(paramnumberOut))
    r=f(byref(t[0]),byref(t[1]),byref(t[2]))
    return (r,int(t[0].value),int(t[1].value),int(t[2].value))
     
def RPR_GetLastTouchedTrack():
    """
    Python: MediaTrack  RPR_GetLastTouchedTrack()
    """
    a=_ft['GetLastTouchedTrack']
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetMainHwnd():
    """
    Python: HWND  RPR_GetMainHwnd()
    """
    a=_ft['GetMainHwnd']
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('HWND',r)
     
def RPR_GetMasterMuteSoloFlags():
    """
    Python: Int  RPR_GetMasterMuteSoloFlags()
    
    &1=master mute,&2=master solo. This is deprecated as you can just query the master track as well.
    """
    a=_ft['GetMasterMuteSoloFlags']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetMasterTrack(proj):
    """
    Python: MediaTrack  RPR_GetMasterTrack(ReaProject proj)
    """
    a=_ft['GetMasterTrack']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetMasterTrackVisibility():
    """
    Python: Int  RPR_GetMasterTrackVisibility()
    
    returns &1 if the master track is visible in the TCP, &2 if visible in the mixer. See SetMasterTrackVisibility
    .
    """
    a=_ft['GetMasterTrackVisibility']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetMaxMidiInputs():
    """
    Python: Int  RPR_GetMaxMidiInputs()
    
    returns max dev for midi inputs/outputs
    """
    a=_ft['GetMaxMidiInputs']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetMaxMidiOutputs():
    """
    Python: Int  RPR_GetMaxMidiOutputs()
    """
    a=_ft['GetMaxMidiOutputs']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetMediaItem(proj,itemidx):
    """
    Python: MediaItem  RPR_GetMediaItem(ReaProject proj, Int itemidx)
    
    get an item from a project by item count (zero-based) (proj=0 for active project)
    """
    a=_ft['GetMediaItem']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(itemidx))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem*',r)
     
def RPR_GetMediaItem_Track(item):
    """
    Python: MediaTrack  RPR_GetMediaItem_Track(MediaItem item)
    
    Get parent track of media item
    """
    a=_ft['GetMediaItem_Track']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetMediaItemInfo_Value(item,parmname):
    """
    Python: Float  RPR_GetMediaItemInfo_Value(MediaItem item, String parmname)
    
    Get media item numerical-value attributes.
    
    B_MUTE : bool * to muted state
    
    B_LOOPSRC : bool * to loop source
    
    B_ALLTAKESPLAY : bool * to all takes play
    
    B_UISEL : bool * to ui selected
    
    C_BEATATTACHMODE : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsosonly
    
    C_LOCK : char * to one char of lock flags (&1 is locked, currently)
    
    D_VOL : double * of item volume (volume bar)
    
    D_POSITION : double * of item position (seconds)
    
    D_LENGTH : double * of item length (seconds)
    
    D_SNAPOFFSET : double * of item snap offset (seconds)
    
    D_FADEINLEN : double * of item fade in length (manual, seconds)
    
    D_FADEOUTLEN : double * of item fade out length (manual, seconds)
    
    D_FADEINDIR : double * of item fade in curve [-1; 1]
    
    D_FADEOUTDIR : double * of item fade out curve [-1; 1]
    
    D_FADEINLEN_AUTO : double * of item autofade in length (seconds, -1 for no autofade set)
    
    D_FADEOUTLEN_AUTO : double * of item autofade out length (seconds, -1 for no autofade set)
    
    C_FADEINSHAPE : int * to fadein shape, 0=linear, ...
    
    C_FADEOUTSHAPE : int * to fadeout shape
    
    I_GROUPID : int * to group ID (0 = no group)
    
    I_LASTY : int * to last y position in track (readonly)
    
    I_LASTH : int * to last height in track (readonly)
    
    I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    
    I_CURTAKE : int * to active take
    
    IP_ITEMNUMBER : int, item number within the track (read-only, returns the item number directly)
    
    F_FREEMODE_Y : float * to free mode y position (0..1)
    
    F_FREEMODE_H : float * to free mode height (0..1)
    
    P_TRACK : MediaTrack * (read only)
    """
    a=_ft['GetMediaItemInfo_Value']
    f=CFUNCTYPE(c_double,c_uint64,c_char_p)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packsc(parmname))
    r=f(t[0],t[1])
    return r
     
def RPR_GetMediaItemNumTakes(item):
    """
    Python: Int  RPR_GetMediaItemNumTakes(MediaItem item)
    """
    a=_ft['GetMediaItemNumTakes']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def RPR_GetMediaItemTake(item,tk):
    """
    Python: MediaItem_Take  RPR_GetMediaItemTake(MediaItem item, Int tk)
    """
    a=_ft['GetMediaItemTake']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem*',item),c_int(tk))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem_Take*',r)
     
def RPR_GetMediaItemTake_Item(take):
    """
    Python: MediaItem  RPR_GetMediaItemTake_Item(MediaItem_Take take)
    
    Get parent item of media item take
    """
    a=_ft['GetMediaItemTake_Item']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return rpr_unpackp('MediaItem*',r)
     
def RPR_GetMediaItemTake_Peaks(take,peakrate,starttime,numchannels,numsamplesperchannel,want_extra_type,buf):
    """
    Python: (Int retval, MediaItem_Take take, Float peakrate, Float starttime, Int numchannels, Int numsamplesperchannel, Int want_extra_type, Float buf) = RPR_GetMediaItemTake_Peaks(take, peakrate, starttime, numchannels, numsamplesperchannel, want_extra_type, buf)
    
    Gets block of peak samples to buf. Note that the peak samples are interleaved, but in two or three blocks (maximums, then minimums, then extra). Return value has 20 bits of returned sample count, then 4 bits of output_mode (0xf00000), then a bit to signify whether extra_type was available (0x1000000). extra_type can be 115 ('s') for spectral information, which will return peak samples as integers with the low 15 bits frequency, next 14 bits tonality.
    """
    a=_ft['GetMediaItemTake_Peaks']
    f=CFUNCTYPE(c_int,c_uint64,c_double,c_double,c_int,c_int,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(peakrate),c_double(starttime),c_int(numchannels),c_int(numsamplesperchannel),c_int(want_extra_type),c_double(buf))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],byref(t[6]))
    return (r,take,peakrate,starttime,numchannels,numsamplesperchannel,want_extra_type,float(t[6].value))
     
def RPR_GetMediaItemTake_Source(take):
    """
    Python: PCM_source  RPR_GetMediaItemTake_Source(MediaItem_Take take)
    
    Get media source of media item take
    """
    a=_ft['GetMediaItemTake_Source']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return rpr_unpackp('PCM_source*',r)
     
def RPR_GetMediaItemTake_Track(take):
    """
    Python: MediaTrack  RPR_GetMediaItemTake_Track(MediaItem_Take take)
    
    Get parent track of media item take
    """
    a=_ft['GetMediaItemTake_Track']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetMediaItemTakeByGUID(project,guid):
    """
    Python: MediaItem_Take  RPR_GetMediaItemTakeByGUID(ReaProject project, const GUID guid)
    """
    a=_ft['GetMediaItemTakeByGUID']
    f=CFUNCTYPE(c_uint64,c_uint64,c_uint64)(a)
    t=(rpr_packp('ReaProject*',project),rpr_packp('GUID*',guid))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem_Take*',r)
     
def RPR_GetMediaItemTakeInfo_Value(take,parmname):
    """
    Python: Float  RPR_GetMediaItemTakeInfo_Value(MediaItem_Take take, String parmname)
    
    Get media item take numerical-value attributes.
    
    D_STARTOFFS : double *, start offset in take of item
    
    D_VOL : double *, take volume
    
    D_PAN : double *, take pan
    
    D_PANLAW : double *, take pan law (-1.0=default, 0.5=-6dB, 1.0=+0dB, etc)
    
    D_PLAYRATE : double *, take playrate (1.0=normal, 2.0=doublespeed, etc)
    
    D_PITCH : double *, take pitch adjust (in semitones, 0.0=normal, +12 = one octave up, etc)
    
    B_PPITCH, bool *, preserve pitch when changing rate
    
    I_CHANMODE, int *, channel mode (0=normal, 1=revstereo, 2=downmix, 3=l, 4=r)
    
    I_PITCHMODE, int *, pitch shifter mode, -1=proj default, otherwise high word=shifter low word = parameter
    
    I_CUSTOMCOLOR : int *, custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    
    IP_TAKENUMBER : int, take number within the item (read-only, returns the take number directly)
    
    P_TRACK : pointer to MediaTrack (read-only)
    
    P_ITEM : pointer to MediaItem (read-only)
    
    P_SOURCE : PCM_source *. Note that if setting this, you should first retrieve the old source, set the new, THEN delete the old.
    """
    a=_ft['GetMediaItemTakeInfo_Value']
    f=CFUNCTYPE(c_double,c_uint64,c_char_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packsc(parmname))
    r=f(t[0],t[1])
    return r
     
def RPR_GetMediaItemTrack(item):
    """
    Python: MediaTrack  RPR_GetMediaItemTrack(MediaItem item)
    """
    a=_ft['GetMediaItemTrack']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetMediaSourceFileName(source,filenamebuf,filenamebuf_sz):
    """
    Python: (PCM_source source, String filenamebuf, Int filenamebuf_sz) = RPR_GetMediaSourceFileName(source, filenamebuf, filenamebuf_sz)
    
    Copies the media source filename to typebuf. Note that in-project MIDI media sources have no associated filename. See GetMediaSourceParent
    .
    """
    a=_ft['GetMediaSourceFileName']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('PCM_source*',source),rpr_packs(filenamebuf),c_int(filenamebuf_sz))
    f(t[0],t[1],t[2])
    return (source,rpr_unpacks(t[1]),filenamebuf_sz)
     
def RPR_GetMediaSourceLength(source,lengthIsQNOut):
    """
    Python: (Float retval, PCM_source source, Boolean lengthIsQNOut) = RPR_GetMediaSourceLength(source, lengthIsQNOut)
    
    Returns the length of the source media. If the media source is beat-based, the length will be in quarter notes, otherwise it will be in seconds.
    """
    a=_ft['GetMediaSourceLength']
    f=CFUNCTYPE(c_double,c_uint64,c_void_p)(a)
    t=(rpr_packp('PCM_source*',source),c_byte(lengthIsQNOut))
    r=f(t[0],byref(t[1]))
    return (r,source,int(t[1].value))
     
def RPR_GetMediaSourceNumChannels(source):
    """
    Python: Int  RPR_GetMediaSourceNumChannels(PCM_source source)
    
    Returns the number of channels in the source media.
    """
    a=_ft['GetMediaSourceNumChannels']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('PCM_source*',source),)
    r=f(t[0])
    return r
     
def RPR_GetMediaSourceParent(src):
    """
    Python: PCM_source  RPR_GetMediaSourceParent(PCM_source src)
    
    Returns the parent source, or NULL if src is the root source. This can be used to retrieve the parent properties of sections or reversed sources for example.
    """
    a=_ft['GetMediaSourceParent']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('PCM_source*',src),)
    r=f(t[0])
    return rpr_unpackp('PCM_source*',r)
     
def RPR_GetMediaSourceSampleRate(source):
    """
    Python: Int  RPR_GetMediaSourceSampleRate(PCM_source source)
    
    Returns the sample rate. MIDI source media will return zero.
    """
    a=_ft['GetMediaSourceSampleRate']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('PCM_source*',source),)
    r=f(t[0])
    return r
     
def RPR_GetMediaSourceType(source,typebuf,typebuf_sz):
    """
    Python: (PCM_source source, String typebuf, Int typebuf_sz) = RPR_GetMediaSourceType(source, typebuf, typebuf_sz)
    
    copies the media source type ("WAV", "MIDI", etc) to typebuf
    """
    a=_ft['GetMediaSourceType']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('PCM_source*',source),rpr_packs(typebuf),c_int(typebuf_sz))
    f(t[0],t[1],t[2])
    return (source,rpr_unpacks(t[1]),typebuf_sz)
     
def RPR_GetMediaTrackInfo_Value(tr,parmname):
    """
    Python: Float  RPR_GetMediaTrackInfo_Value(MediaTrack tr, String parmname)
    
    Get track numerical-value attributes.
    
    B_MUTE : bool * : mute flag
    
    B_PHASE : bool * : invert track phase
    
    IP_TRACKNUMBER : int : track number (returns zero if not found, -1 for master track) (read-only, returns the int directly)
    
    I_SOLO : int * : 0=not soloed, 1=solo, 2=soloed in place. also: 5=solo-safe solo, 6=solo-safe soloed in place
    
    I_FXEN : int * : 0=fx bypassed, nonzero = fx active
    
    I_RECARM : int * : 0=not record armed, 1=record armed
    
    I_RECINPUT : int * : record input. <0 = no input, 0..n = mono hardware input, 512+n = rearoute input, 1024 set for stereo input pair. 4096 set for MIDI input, if set, then low 5 bits represent channel (0=all, 1-16=only chan), then next 6 bits represent physical input (63=all, 62=VKB)
    
    I_RECMODE : int * : record mode (0=input, 1=stereo out, 2=none, 3=stereo out w/latcomp, 4=midi output, 5=mono out, 6=mono out w/ lat comp, 7=midi overdub, 8=midi replace
    
    I_RECMON : int * : record monitor (0=off, 1=normal, 2=not when playing (tapestyle))
    
    I_RECMONITEMS : int * : monitor items while recording (0=off, 1=on)
    
    I_AUTOMODE : int * : track automation mode (0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
    
    I_NCHAN : int * : number of track channels, must be 2-64, even
    
    I_SELECTED : int * : track selected? 0 or 1
    
    I_WNDH : int * : current TCP window height (Read-only)
    
    I_FOLDERDEPTH : int * : folder depth change (0=normal, 1=track is a folder parent, -1=track is the last in the innermost folder, -2=track is the last in the innermost and next-innermost folders, etc
    
    I_FOLDERCOMPACT : int * : folder compacting (only valid on folders), 0=normal, 1=small, 2=tiny children
    
    I_MIDIHWOUT : int * : track midi hardware output index (<0 for disabled, low 5 bits are which channels (0=all, 1-16), next 5 bits are output device index (0-31))
    
    I_PERFFLAGS : int * : track perf flags (&1=no media buffering, &2=no anticipative FX)
    
    I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    
    I_HEIGHTOVERRIDE : int * : custom height override for TCP window. 0 for none, otherwise size in pixels
    
    B_HEIGHTLOCK : bool * : track height lock (must set I_HEIGHTOVERRIDE before locking)
    
    D_VOL : double * : trim volume of track (0 (-inf)..1 (+0dB) .. 2 (+6dB) etc ..)
    
    D_PAN : double * : trim pan of track (-1..1)
    
    D_WIDTH : double * : width of track (-1..1)
    
    D_DUALPANL : double * : dualpan position 1 (-1..1), only if I_PANMODE==6
    
    D_DUALPANR : double * : dualpan position 2 (-1..1), only if I_PANMODE==6
    
    I_PANMODE : int * : pan mode (0 = classic 3.x, 3=new balance, 5=stereo pan, 6 = dual pan)
    
    D_PANLAW : double * : pan law of track. <0 for project default, 1.0 for +0dB, etc
    
    P_ENV : read only, returns TrackEnvelope *, setNewValue=<VOLENV, <PANENV, etc
    
    B_SHOWINMIXER : bool * : show track panel in mixer -- do not use on master
    
    B_SHOWINTCP : bool * : show track panel in tcp -- do not use on master
    
    B_MAINSEND : bool * : track sends audio to parent
    
    C_MAINSEND_OFFS : char * : track send to parent channel offset
    
    B_FREEMODE : bool * : track free-mode enabled (requires UpdateTimeline() after changing etc)
    
    C_BEATATTACHMODE : char * : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsposonly
    
    F_MCP_FXSEND_SCALE : float * : scale of fx+send area in MCP (0.0=smallest allowed, 1=max allowed)
    
    F_MCP_SENDRGN_SCALE : float * : scale of send area as proportion of the fx+send total area (0=min allow, 1=max)
    
    P_PARTRACK : MediaTrack * : parent track (read-only)
    
    P_PROJECT : ReaProject * : parent project (read-only)
    """
    a=_ft['GetMediaTrackInfo_Value']
    f=CFUNCTYPE(c_double,c_uint64,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packsc(parmname))
    r=f(t[0],t[1])
    return r
     
def RPR_GetMIDIInputName(dev,nameout,nameout_sz):
    """
    Python: (Boolean retval, Int dev, String nameout, Int nameout_sz) = RPR_GetMIDIInputName(dev, nameout, nameout_sz)
    
    returns true if device present
    """
    a=_ft['GetMIDIInputName']
    f=CFUNCTYPE(c_byte,c_int,c_char_p,c_int)(a)
    t=(c_int(dev),rpr_packs(nameout),c_int(nameout_sz))
    r=f(t[0],t[1],t[2])
    return (r,dev,rpr_unpacks(t[1]),nameout_sz)
     
def RPR_GetMIDIOutputName(dev,nameout,nameout_sz):
    """
    Python: (Boolean retval, Int dev, String nameout, Int nameout_sz) = RPR_GetMIDIOutputName(dev, nameout, nameout_sz)
    
    returns true if device present
    """
    a=_ft['GetMIDIOutputName']
    f=CFUNCTYPE(c_byte,c_int,c_char_p,c_int)(a)
    t=(c_int(dev),rpr_packs(nameout),c_int(nameout_sz))
    r=f(t[0],t[1],t[2])
    return (r,dev,rpr_unpacks(t[1]),nameout_sz)
     
def RPR_GetMixerScroll():
    """
    Python: MediaTrack  RPR_GetMixerScroll()
    
    Get the leftmost track visible in the mixer
    """
    a=_ft['GetMixerScroll']
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetMouseModifier(context,modifier_flag,action,action_sz):
    """
    Python: (String context, Int modifier_flag, String action, Int action_sz) = RPR_GetMouseModifier(context, modifier_flag, action, action_sz)
    
    Get the current mouse modifier assignment for a specific modifier key assignment, in a specific context.
    
    action will be filled in with the command ID number for a built-in mouse modifier
    
    or built-in REAPER command ID, or the custom action ID string.
    
    See SetMouseModifier
     for more information.
    """
    a=_ft['GetMouseModifier']
    f=CFUNCTYPE(None,c_char_p,c_int,c_char_p,c_int)(a)
    t=(rpr_packsc(context),c_int(modifier_flag),rpr_packs(action),c_int(action_sz))
    f(t[0],t[1],t[2],t[3])
    return (context,modifier_flag,rpr_unpacks(t[2]),action_sz)
     
def RPR_GetMousePosition(xOut,yOut):
    """
    Python: (Int xOut, Int yOut) = RPR_GetMousePosition(xOut, yOut)
    
    get mouse position in screen coordinates
    """
    a=_ft['GetMousePosition']
    f=CFUNCTYPE(None,c_void_p,c_void_p)(a)
    t=(c_int(xOut),c_int(yOut))
    f(byref(t[0]),byref(t[1]))
    return (int(t[0].value),int(t[1].value))
     
def RPR_GetNumAudioInputs():
    """
    Python: Int  RPR_GetNumAudioInputs()
    
    Return number of normal audio hardware inputs available
    """
    a=_ft['GetNumAudioInputs']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetNumAudioOutputs():
    """
    Python: Int  RPR_GetNumAudioOutputs()
    
    Return number of normal audio hardware outputs available
    """
    a=_ft['GetNumAudioOutputs']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetNumMIDIInputs():
    """
    Python: Int  RPR_GetNumMIDIInputs()
    
    returns max number of real midi hardware inputs
    """
    a=_ft['GetNumMIDIInputs']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetNumMIDIOutputs():
    """
    Python: Int  RPR_GetNumMIDIOutputs()
    
    returns max number of real midi hardware outputs
    """
    a=_ft['GetNumMIDIOutputs']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetNumTracks():
    """
    Python: Int  RPR_GetNumTracks()
    """
    a=_ft['GetNumTracks']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetOS():
    """
    Python: String  RPR_GetOS()
    
    Returns "Win32", "Win64", "OSX32", "OSX64", or "Other".
    """
    a=_ft['GetOS']
    f=CFUNCTYPE(c_char_p)(a)
    r=f()
    return str(r.decode())
     
def RPR_GetOutputChannelName(channelIndex):
    """
    Python: String  RPR_GetOutputChannelName(Int channelIndex)
    """
    a=_ft['GetOutputChannelName']
    f=CFUNCTYPE(c_char_p,c_int)(a)
    t=(c_int(channelIndex),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_GetOutputLatency():
    """
    Python: Float  RPR_GetOutputLatency()
    
    returns output latency in seconds
    """
    a=_ft['GetOutputLatency']
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def RPR_GetParentTrack(track):
    """
    Python: MediaTrack  RPR_GetParentTrack(MediaTrack track)
    """
    a=_ft['GetParentTrack']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetPeakFileName(fn,buf,buf_sz):
    """
    Python: (String fn, String buf, Int buf_sz) = RPR_GetPeakFileName(fn, buf, buf_sz)
    
    get the peak file name for a given file (can be either filename.reapeaks,or a hashed filename in another path)
    """
    a=_ft['GetPeakFileName']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(fn),rpr_packs(buf),c_int(buf_sz))
    f(t[0],t[1],t[2])
    return (fn,rpr_unpacks(t[1]),buf_sz)
     
def RPR_GetPeakFileNameEx(fn,buf,buf_sz,forWrite):
    """
    Python: (String fn, String buf, Int buf_sz, Boolean forWrite) = RPR_GetPeakFileNameEx(fn, buf, buf_sz, forWrite)
    
    get the peak file name for a given file (can be either filename.reapeaks,or a hashed filename in another path)
    """
    a=_ft['GetPeakFileNameEx']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_int,c_byte)(a)
    t=(rpr_packsc(fn),rpr_packs(buf),c_int(buf_sz),c_byte(forWrite))
    f(t[0],t[1],t[2],t[3])
    return (fn,rpr_unpacks(t[1]),buf_sz,forWrite)
     
def RPR_GetPeakFileNameEx2(fn,buf,buf_sz,forWrite,peaksfileextension):
    """
    Python: (String fn, String buf, Int buf_sz, Boolean forWrite, String peaksfileextension) = RPR_GetPeakFileNameEx2(fn, buf, buf_sz, forWrite, peaksfileextension)
    
    Like GetPeakFileNameEx, but you can specify peaksfileextension such as ".reapeaks"
    """
    a=_ft['GetPeakFileNameEx2']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_int,c_byte,c_char_p)(a)
    t=(rpr_packsc(fn),rpr_packs(buf),c_int(buf_sz),c_byte(forWrite),rpr_packsc(peaksfileextension))
    f(t[0],t[1],t[2],t[3],t[4])
    return (fn,rpr_unpacks(t[1]),buf_sz,forWrite,peaksfileextension)
     
def RPR_GetPlayPosition():
    """
    Python: Float  RPR_GetPlayPosition()
    
    returns latency-compensated actual-what-you-hear position
    """
    a=_ft['GetPlayPosition']
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def RPR_GetPlayPosition2():
    """
    Python: Float  RPR_GetPlayPosition2()
    
    returns position of next audio block being processed
    """
    a=_ft['GetPlayPosition2']
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def RPR_GetPlayPosition2Ex(proj):
    """
    Python: Float  RPR_GetPlayPosition2Ex(ReaProject proj)
    
    returns position of next audio block being processed
    """
    a=_ft['GetPlayPosition2Ex']
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_GetPlayPositionEx(proj):
    """
    Python: Float  RPR_GetPlayPositionEx(ReaProject proj)
    
    returns latency-compensated actual-what-you-hear position
    """
    a=_ft['GetPlayPositionEx']
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_GetPlayState():
    """
    Python: Int  RPR_GetPlayState()
    
    &1=playing,&2=pause,&=4 is recording
    """
    a=_ft['GetPlayState']
    f=CFUNCTYPE(c_int)(a)
    r=f()
    return r
     
def RPR_GetPlayStateEx(proj):
    """
    Python: Int  RPR_GetPlayStateEx(ReaProject proj)
    
    &1=playing,&2=pause,&=4 is recording
    """
    a=_ft['GetPlayStateEx']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_GetProjectLength(proj):
    """
    Python: Float  RPR_GetProjectLength(ReaProject proj)
    
    returns length of project (maximum of end of media item, markers, end of regions, tempo map
    """
    a=_ft['GetProjectLength']
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_GetProjectName(proj,buf,buf_sz):
    """
    Python: (ReaProject proj, String buf, Int buf_sz) = RPR_GetProjectName(proj, buf, buf_sz)
    """
    a=_ft['GetProjectName']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packs(buf),c_int(buf_sz))
    f(t[0],t[1],t[2])
    return (proj,rpr_unpacks(t[1]),buf_sz)
     
def RPR_GetProjectPath(buf,buf_sz):
    """
    Python: (String buf, Int buf_sz) = RPR_GetProjectPath(buf, buf_sz)
    """
    a=_ft['GetProjectPath']
    f=CFUNCTYPE(None,c_char_p,c_int)(a)
    t=(rpr_packs(buf),c_int(buf_sz))
    f(t[0],t[1])
    return (rpr_unpacks(t[0]),buf_sz)
     
def RPR_GetProjectPathEx(proj,buf,buf_sz):
    """
    Python: (ReaProject proj, String buf, Int buf_sz) = RPR_GetProjectPathEx(proj, buf, buf_sz)
    """
    a=_ft['GetProjectPathEx']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packs(buf),c_int(buf_sz))
    f(t[0],t[1],t[2])
    return (proj,rpr_unpacks(t[1]),buf_sz)
     
def RPR_GetProjectStateChangeCount(proj):
    """
    Python: Int  RPR_GetProjectStateChangeCount(ReaProject proj)
    
    returns an integer that changes when the project state changes
    """
    a=_ft['GetProjectStateChangeCount']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_GetProjectTimeOffset(proj,rndframe):
    """
    Python: Float  RPR_GetProjectTimeOffset(ReaProject proj, Boolean rndframe)
    
    Gets project time offset in seconds (project settings - project start time). If rndframe is true, the offset is rounded to a multiple of the project frame size.
    """
    a=_ft['GetProjectTimeOffset']
    f=CFUNCTYPE(c_double,c_uint64,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(rndframe))
    r=f(t[0],t[1])
    return r
     
def RPR_GetProjectTimeSignature(bpmOut,bpiOut):
    """
    Python: (Float bpmOut, Float bpiOut) = RPR_GetProjectTimeSignature(bpmOut, bpiOut)
    
    deprecated
    """
    a=_ft['GetProjectTimeSignature']
    f=CFUNCTYPE(None,c_void_p,c_void_p)(a)
    t=(c_double(bpmOut),c_double(bpiOut))
    f(byref(t[0]),byref(t[1]))
    return (float(t[0].value),float(t[1].value))
     
def RPR_GetProjectTimeSignature2(proj,bpmOut,bpiOut):
    """
    Python: (ReaProject proj, Float bpmOut, Float bpiOut) = RPR_GetProjectTimeSignature2(proj, bpmOut, bpiOut)
    
    Gets basic time signature (beats per minute, numerator of time signature in bpi)
    
    this does not reflect tempo envelopes but is purely what is set in the project settings.
    """
    a=_ft['GetProjectTimeSignature2']
    f=CFUNCTYPE(None,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(bpmOut),c_double(bpiOut))
    f(t[0],byref(t[1]),byref(t[2]))
    return (proj,float(t[1].value),float(t[2].value))
     
def RPR_GetProjExtState(proj,extname,key,valOutNeedBig,valOutNeedBig_sz):
    """
    Python: (Int retval, ReaProject proj, String extname, String key, String valOutNeedBig, Int valOutNeedBig_sz) = RPR_GetProjExtState(proj, extname, key, valOutNeedBig, valOutNeedBig_sz)
    
    Get the value previously associated with this extname and key, the last time the project was saved. See SetProjExtState
    , EnumProjExtState
    .
    """
    a=_ft['GetProjExtState']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(extname),rpr_packsc(key),rpr_packs(valOutNeedBig),c_int(valOutNeedBig_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,proj,extname,key,rpr_unpacks(t[3]),valOutNeedBig_sz)
     
def RPR_GetResourcePath():
    """
    Python: String  RPR_GetResourcePath()
    
    returns path where ini files are stored, other things are in subdirectories.
    """
    a=_ft['GetResourcePath']
    f=CFUNCTYPE(c_char_p)(a)
    r=f()
    return str(r.decode())
     
def RPR_GetSelectedEnvelope(proj):
    """
    Python: TrackEnvelope  RPR_GetSelectedEnvelope(ReaProject proj)
    
    get the currently selected envelope, returns 0 if no envelope is selected
    """
    a=_ft['GetSelectedEnvelope']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetSelectedMediaItem(proj,selitem):
    """
    Python: MediaItem  RPR_GetSelectedMediaItem(ReaProject proj, Int selitem)
    
    get a selected item by selected item count (zero-based) (proj=0 for active project)
    """
    a=_ft['GetSelectedMediaItem']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(selitem))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem*',r)
     
def RPR_GetSelectedTrack(proj,seltrackidx):
    """
    Python: MediaTrack  RPR_GetSelectedTrack(ReaProject proj, Int seltrackidx)
    
    Get a selected track from a project (proj=0 for active project) by selected track count (zero-based). This function ignores the master track, see GetSelectedTrack2
    .
    """
    a=_ft['GetSelectedTrack']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(seltrackidx))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetSelectedTrack2(proj,seltrackidx,wantmaster):
    """
    Python: MediaTrack  RPR_GetSelectedTrack2(ReaProject proj, Int seltrackidx, Boolean wantmaster)
    
    Get a selected track from a project (proj=0 for active project) by selected track count (zero-based).
    """
    a=_ft['GetSelectedTrack2']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(seltrackidx),c_byte(wantmaster))
    r=f(t[0],t[1],t[2])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetSelectedTrackEnvelope(proj):
    """
    Python: TrackEnvelope  RPR_GetSelectedTrackEnvelope(ReaProject proj)
    
    get the currently selected track envelope, returns 0 if no envelope is selected
    """
    a=_ft['GetSelectedTrackEnvelope']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetSet_ArrangeView2(proj,isSet,screen_x_start,screen_x_end,start_timeOut,end_timeOut):
    """
    Python: (ReaProject proj, Boolean isSet, Int screen_x_start, Int screen_x_end, Float start_timeOut, Float end_timeOut) = RPR_GetSet_ArrangeView2(proj, isSet, screen_x_start, screen_x_end, start_timeOut, end_timeOut)
    
    Gets or sets the arrange view start/end time for screen coordinates. use screen_x_start=screen_x_end=0 to use the full arrange view's start/end time
    """
    a=_ft['GetSet_ArrangeView2']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_int,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(isSet),c_int(screen_x_start),c_int(screen_x_end),c_double(start_timeOut),c_double(end_timeOut))
    f(t[0],t[1],t[2],t[3],byref(t[4]),byref(t[5]))
    return (proj,isSet,screen_x_start,screen_x_end,float(t[4].value),float(t[5].value))
     
def RPR_GetSet_LoopTimeRange(isSet,isLoop,startOut,endOut,allowautoseek):
    """
    Python: (Boolean isSet, Boolean isLoop, Float startOut, Float endOut, Boolean allowautoseek) = RPR_GetSet_LoopTimeRange(isSet, isLoop, startOut, endOut, allowautoseek)
    """
    a=_ft['GetSet_LoopTimeRange']
    f=CFUNCTYPE(None,c_byte,c_byte,c_void_p,c_void_p,c_byte)(a)
    t=(c_byte(isSet),c_byte(isLoop),c_double(startOut),c_double(endOut),c_byte(allowautoseek))
    f(t[0],t[1],byref(t[2]),byref(t[3]),t[4])
    return (isSet,isLoop,float(t[2].value),float(t[3].value),allowautoseek)
     
def RPR_GetSet_LoopTimeRange2(proj,isSet,isLoop,startOut,endOut,allowautoseek):
    """
    Python: (ReaProject proj, Boolean isSet, Boolean isLoop, Float startOut, Float endOut, Boolean allowautoseek) = RPR_GetSet_LoopTimeRange2(proj, isSet, isLoop, startOut, endOut, allowautoseek)
    """
    a=_ft['GetSet_LoopTimeRange2']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_byte,c_void_p,c_void_p,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(isSet),c_byte(isLoop),c_double(startOut),c_double(endOut),c_byte(allowautoseek))
    f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),t[5])
    return (proj,isSet,isLoop,float(t[3].value),float(t[4].value),allowautoseek)
     
def RPR_GetSetAutomationItemInfo(env,autoitem_idx,desc,value,is_set):
    """
    Python: Float  RPR_GetSetAutomationItemInfo(TrackEnvelope env, Int autoitem_idx, String desc, Float value, Boolean is_set)
    
    Get or set automation item information. autoitem_idx==0 for the first automation item on an envelope, 1 for the second item, etc. desc can be any of the following:
    
    D_POOL_ID: double *, automation item pool ID (as an integer); edits are propagated to all other automation items that share a pool ID
    
    D_POSITION: double *, automation item timeline position in seconds
    
    D_LENGTH: double *, automation item length in seconds
    
    D_STARTOFFS: double *, automation item start offset in seconds
    
    D_PLAYRATE: double *, automation item playback rate
    
    D_BASELINE: double *, automation item baseline value in the range [0,1]
    
    D_AMPLITUDE: double *, automation item amplitude in the range [-1,1]
    
    D_LOOPSRC: double *, nonzero if the automation item contents are looped
    
    D_UISEL: double *, nonzero if the automation item is selected in the arrange view
    """
    a=_ft['GetSetAutomationItemInfo']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_char_p,c_double,c_byte)(a)
    t=(rpr_packp('TrackEnvelope*',env),c_int(autoitem_idx),rpr_packsc(desc),c_double(value),c_byte(is_set))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def RPR_GetSetEnvelopeState(env,Str,str_sz):
    """
    Python: (Boolean retval, TrackEnvelope env, String str, Int str_sz) = RPR_GetSetEnvelopeState(env, str, str_sz)
    
    deprecated -- see SetEnvelopeStateChunk
    , GetEnvelopeStateChunk
    """
    a=_ft['GetSetEnvelopeState']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('TrackEnvelope*',env),rpr_packs(Str),c_int(str_sz))
    r=f(t[0],t[1],t[2])
    return (r,env,rpr_unpacks(t[1]),str_sz)
     
def RPR_GetSetEnvelopeState2(env,Str,str_sz,isundo):
    """
    Python: (Boolean retval, TrackEnvelope env, String str, Int str_sz, Boolean isundo) = RPR_GetSetEnvelopeState2(env, str, str_sz, isundo)
    
    deprecated -- see SetEnvelopeStateChunk
    , GetEnvelopeStateChunk
    """
    a=_ft['GetSetEnvelopeState2']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_byte)(a)
    t=(rpr_packp('TrackEnvelope*',env),rpr_packs(Str),c_int(str_sz),c_byte(isundo))
    r=f(t[0],t[1],t[2],t[3])
    return (r,env,rpr_unpacks(t[1]),str_sz,isundo)
     
def RPR_GetSetItemState(item,Str,str_sz):
    """
    Python: (Boolean retval, MediaItem item, String str, Int str_sz) = RPR_GetSetItemState(item, str, str_sz)
    
    deprecated -- see SetItemStateChunk
    , GetItemStateChunk
    """
    a=_ft['GetSetItemState']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packs(Str),c_int(str_sz))
    r=f(t[0],t[1],t[2])
    return (r,item,rpr_unpacks(t[1]),str_sz)
     
def RPR_GetSetItemState2(item,Str,str_sz,isundo):
    """
    Python: (Boolean retval, MediaItem item, String str, Int str_sz, Boolean isundo) = RPR_GetSetItemState2(item, str, str_sz, isundo)
    
    deprecated -- see SetItemStateChunk
    , GetItemStateChunk
    """
    a=_ft['GetSetItemState2']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packs(Str),c_int(str_sz),c_byte(isundo))
    r=f(t[0],t[1],t[2],t[3])
    return (r,item,rpr_unpacks(t[1]),str_sz,isundo)
     
def RPR_GetSetMediaItemInfo_String(item,parmname,stringNeedBig,setNewValue):
    """
    Python: (Boolean retval, MediaItem item, String parmname, String stringNeedBig, Boolean setNewValue) = RPR_GetSetMediaItemInfo_String(item, parmname, stringNeedBig, setNewValue)
    
    Gets/sets an item attribute string:
    
    P_NOTES : char * : item note text (do not write to returned pointer, use setNewValue to update)
    
    GUID : GUID * : 16-byte GUID, can query or update. If using a _String() function, GUID is a string {xyz-...}.
    """
    a=_ft['GetSetMediaItemInfo_String']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_char_p,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packsc(parmname),rpr_packs(stringNeedBig),c_byte(setNewValue))
    r=f(t[0],t[1],t[2],t[3])
    return (r,item,parmname,rpr_unpacks(t[2]),setNewValue)
     
def RPR_GetSetMediaItemTakeInfo_String(tk,parmname,stringNeedBig,setNewValue):
    """
    Python: (Boolean retval, MediaItem_Take tk, String parmname, String stringNeedBig, Boolean setNewValue) = RPR_GetSetMediaItemTakeInfo_String(tk, parmname, stringNeedBig, setNewValue)
    
    Gets/sets a take attribute string:
    
    P_NAME : char * to take name
    
    GUID : GUID * : 16-byte GUID, can query or update. If using a _String() function, GUID is a string {xyz-...}.
    """
    a=_ft['GetSetMediaItemTakeInfo_String']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_char_p,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',tk),rpr_packsc(parmname),rpr_packs(stringNeedBig),c_byte(setNewValue))
    r=f(t[0],t[1],t[2],t[3])
    return (r,tk,parmname,rpr_unpacks(t[2]),setNewValue)
     
def RPR_GetSetMediaTrackInfo_String(tr,parmname,stringNeedBig,setNewValue):
    """
    Python: (Boolean retval, MediaTrack tr, String parmname, String stringNeedBig, Boolean setNewValue) = RPR_GetSetMediaTrackInfo_String(tr, parmname, stringNeedBig, setNewValue)
    
    Get or set track string attributes.
    
    P_NAME : char * : track name (on master returns NULL)
    
    P_ICON : const char * : track icon (full filename, or relative to resource_path/data/track_icons)
    
    P_MCP_LAYOUT : const char * : layout name
    
    P_TCP_LAYOUT : const char * : layout name
    
    GUID : GUID * : 16-byte GUID, can query or update. If using a _String() function, GUID is a string {xyz-...}.
    """
    a=_ft['GetSetMediaTrackInfo_String']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_char_p,c_byte)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packsc(parmname),rpr_packs(stringNeedBig),c_byte(setNewValue))
    r=f(t[0],t[1],t[2],t[3])
    return (r,tr,parmname,rpr_unpacks(t[2]),setNewValue)
     
def RPR_GetSetProjectAuthor(proj,Set,author,author_sz):
    """
    Python: (ReaProject proj, Boolean set, String author, Int author_sz) = RPR_GetSetProjectAuthor(proj, set, author, author_sz)
    
    gets or sets project author, author_sz is ignored when setting
    """
    a=_ft['GetSetProjectAuthor']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(Set),rpr_packs(author),c_int(author_sz))
    f(t[0],t[1],t[2],t[3])
    return (proj,Set,rpr_unpacks(t[2]),author_sz)
     
def RPR_GetSetProjectGrid(project,Set,divisionInOutOptional,swingmodeInOutOptional,swingamtInOutOptional):
    """
    Python: (Int retval, ReaProject project, Boolean set, Float divisionInOutOptional, Int swingmodeInOutOptional, Float swingamtInOutOptional) = RPR_GetSetProjectGrid(project, set, divisionInOutOptional, swingmodeInOutOptional, swingamtInOutOptional)
    
    Get or set the arrange view grid division. 0.25=quarter note, 1.0/3.0=half note triplet, etc. swingmode can be 1 for swing enabled, swingamt is -1..1. Returns grid configuration flags
    """
    a=_ft['GetSetProjectGrid']
    f=CFUNCTYPE(c_int,c_uint64,c_byte,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',project),c_byte(Set),c_double(divisionInOutOptional),c_int(swingmodeInOutOptional),c_double(swingamtInOutOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]))
    return (r,project,Set,float(t[2].value),int(t[3].value),float(t[4].value))
     
def RPR_GetSetProjectNotes(proj,Set,notesNeedBig,notesNeedBig_sz):
    """
    Python: (ReaProject proj, Boolean set, String notesNeedBig, Int notesNeedBig_sz) = RPR_GetSetProjectNotes(proj, set, notesNeedBig, notesNeedBig_sz)
    
    gets or sets project notes, notesNeedBig_sz is ignored when setting
    """
    a=_ft['GetSetProjectNotes']
    f=CFUNCTYPE(None,c_uint64,c_byte,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(Set),rpr_packs(notesNeedBig),c_int(notesNeedBig_sz))
    f(t[0],t[1],t[2],t[3])
    return (proj,Set,rpr_unpacks(t[2]),notesNeedBig_sz)
     
def RPR_GetSetRepeat(val):
    """
    Python: Int  RPR_GetSetRepeat(Int val)
    
    -1 == query,0=clear,1=set,>1=toggle . returns new value
    """
    a=_ft['GetSetRepeat']
    f=CFUNCTYPE(c_int,c_int)(a)
    t=(c_int(val),)
    r=f(t[0])
    return r
     
def RPR_GetSetRepeatEx(proj,val):
    """
    Python: Int  RPR_GetSetRepeatEx(ReaProject proj, Int val)
    
    -1 == query,0=clear,1=set,>1=toggle . returns new value
    """
    a=_ft['GetSetRepeatEx']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(val))
    r=f(t[0],t[1])
    return r
     
def RPR_GetSetTrackGroupMembership(tr,groupname,setmask,setvalue):
    """
    Python: Unknown  RPR_GetSetTrackGroupMembership(MediaTrack tr, String groupname, Unknown setmask, Unknown setvalue)
    
    Gets or modifies the group membership for a track. Returns group state prior to call (each bit represents one of the 32 group numbers). if setmask has bits set, those bits in setvalue will be applied to group. Group can be one of:
    
    VOLUME_MASTER
    
    VOLUME_SLAVE
    
    VOLUME_VCA_MASTER
    
    VOLUME_VCA_SLAVE
    
    PAN_MASTER
    
    PAN_SLAVE
    
    WIDTH_MASTER
    
    WIDTH_SLAVE
    
    MUTE_MASTER
    
    MUTE_SLAVE
    
    SOLO_MASTER
    
    SOLO_SLAVE
    
    RECARM_MASTER
    
    RECARM_SLAVE
    
    POLARITY_MASTER
    
    POLARITY_SLAVE
    
    AUTOMODE_MASTER
    
    AUTOMODE_SLAVE
    
    VOLUME_REVERSE
    
    PAN_REVERSE
    
    WIDTH_REVERSE
    
    NO_MASTER_WHEN_SLAVE
    
    VOLUME_VCA_SLAVE_ISPREFX
    """
    a=_ft['GetSetTrackGroupMembership']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packsc(groupname),c_int(setmask),c_int(setvalue))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_GetSetTrackGroupMembershipHigh(tr,groupname,setmask,setvalue):
    """
    Python: Unknown  RPR_GetSetTrackGroupMembershipHigh(MediaTrack tr, String groupname, Unknown setmask, Unknown setvalue)
    
    Gets or modifies the group membership for a track. Returns group state prior to call (each bit represents one of the high 32 group numbers). if setmask has bits set, those bits in setvalue will be applied to group. Group can be one of:
    
    VOLUME_MASTER
    
    VOLUME_SLAVE
    
    VOLUME_VCA_MASTER
    
    VOLUME_VCA_SLAVE
    
    PAN_MASTER
    
    PAN_SLAVE
    
    WIDTH_MASTER
    
    WIDTH_SLAVE
    
    MUTE_MASTER
    
    MUTE_SLAVE
    
    SOLO_MASTER
    
    SOLO_SLAVE
    
    RECARM_MASTER
    
    RECARM_SLAVE
    
    POLARITY_MASTER
    
    POLARITY_SLAVE
    
    AUTOMODE_MASTER
    
    AUTOMODE_SLAVE
    
    VOLUME_REVERSE
    
    PAN_REVERSE
    
    WIDTH_REVERSE
    
    NO_MASTER_WHEN_SLAVE
    
    VOLUME_VCA_SLAVE_ISPREFX
    """
    a=_ft['GetSetTrackGroupMembershipHigh']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packsc(groupname),c_int(setmask),c_int(setvalue))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_GetSetTrackState(track,Str,str_sz):
    """
    Python: (Boolean retval, MediaTrack track, String str, Int str_sz) = RPR_GetSetTrackState(track, str, str_sz)
    
    deprecated -- see SetTrackStateChunk
    , GetTrackStateChunk
    """
    a=_ft['GetSetTrackState']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packs(Str),c_int(str_sz))
    r=f(t[0],t[1],t[2])
    return (r,track,rpr_unpacks(t[1]),str_sz)
     
def RPR_GetSetTrackState2(track,Str,str_sz,isundo):
    """
    Python: (Boolean retval, MediaTrack track, String str, Int str_sz, Boolean isundo) = RPR_GetSetTrackState2(track, str, str_sz, isundo)
    
    deprecated -- see SetTrackStateChunk
    , GetTrackStateChunk
    """
    a=_ft['GetSetTrackState2']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packs(Str),c_int(str_sz),c_byte(isundo))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,rpr_unpacks(t[1]),str_sz,isundo)
     
def RPR_GetSubProjectFromSource(src):
    """
    Python: ReaProject  RPR_GetSubProjectFromSource(PCM_source src)
    """
    a=_ft['GetSubProjectFromSource']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('PCM_source*',src),)
    r=f(t[0])
    return rpr_unpackp('ReaProject*',r)
     
def RPR_GetTake(item,takeidx):
    """
    Python: MediaItem_Take  RPR_GetTake(MediaItem item, Int takeidx)
    
    get a take from an item by take count (zero-based)
    """
    a=_ft['GetTake']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem*',item),c_int(takeidx))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem_Take*',r)
     
def RPR_GetTakeEnvelope(take,envidx):
    """
    Python: TrackEnvelope  RPR_GetTakeEnvelope(MediaItem_Take take, Int envidx)
    """
    a=_ft['GetTakeEnvelope']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(envidx))
    r=f(t[0],t[1])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetTakeEnvelopeByName(take,envname):
    """
    Python: TrackEnvelope  RPR_GetTakeEnvelopeByName(MediaItem_Take take, String envname)
    """
    a=_ft['GetTakeEnvelopeByName']
    f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packsc(envname))
    r=f(t[0],t[1])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetTakeName(take):
    """
    Python: String  RPR_GetTakeName(MediaItem_Take take)
    
    returns NULL if the take is not valid
    """
    a=_ft['GetTakeName']
    f=CFUNCTYPE(c_char_p,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_GetTakeNumStretchMarkers(take):
    """
    Python: Int  RPR_GetTakeNumStretchMarkers(MediaItem_Take take)
    
    Returns number of stretch markers in take
    """
    a=_ft['GetTakeNumStretchMarkers']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def RPR_GetTakeStretchMarker(take,idx,posOut,srcposOutOptional):
    """
    Python: (Int retval, MediaItem_Take take, Int idx, Float posOut, Float srcposOutOptional) = RPR_GetTakeStretchMarker(take, idx, posOut, srcposOutOptional)
    
    Gets information on a stretch marker, idx is 0..n. Returns false if stretch marker not valid. posOut will be set to position in item, srcposOutOptional will be set to source media position. Returns index. if input index is -1, next marker is found using position (or source position if position is -1). If position/source position are used to find marker position, their values are not updated.
    """
    a=_ft['GetTakeStretchMarker']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(idx),c_double(posOut),c_double(srcposOutOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (r,take,idx,float(t[2].value),float(t[3].value))
     
def RPR_GetTakeStretchMarkerSlope(take,idx):
    """
    Python: Float  RPR_GetTakeStretchMarkerSlope(MediaItem_Take take, Int idx)
    
    See SetTakeStretchMarkerSlope
    """
    a=_ft['GetTakeStretchMarkerSlope']
    f=CFUNCTYPE(c_double,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(idx))
    r=f(t[0],t[1])
    return r
     
def RPR_GetTCPFXParm(project,track,index,fxindexOut,parmidxOut):
    """
    Python: (Boolean retval, ReaProject project, MediaTrack track, Int index, Int fxindexOut, Int parmidxOut) = RPR_GetTCPFXParm(project, track, index, fxindexOut, parmidxOut)
    
    Get information about a specific FX parameter knob (see CountTCPFXParms
    ).
    """
    a=_ft['GetTCPFXParm']
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',project),rpr_packp('MediaTrack*',track),c_int(index),c_int(fxindexOut),c_int(parmidxOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]))
    return (r,project,track,index,int(t[3].value),int(t[4].value))
     
def RPR_GetTempoMatchPlayRate(source,srcscale,position,mult,rateOut,targetlenOut):
    """
    Python: (Boolean retval, PCM_source source, Float srcscale, Float position, Float mult, Float rateOut, Float targetlenOut) = RPR_GetTempoMatchPlayRate(source, srcscale, position, mult, rateOut, targetlenOut)
    
    finds the playrate and target length to insert this item stretched to a round power-of-2 number of bars, between 1/8 and 256
    """
    a=_ft['GetTempoMatchPlayRate']
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_double,c_double,c_void_p,c_void_p)(a)
    t=(rpr_packp('PCM_source*',source),c_double(srcscale),c_double(position),c_double(mult),c_double(rateOut),c_double(targetlenOut))
    r=f(t[0],t[1],t[2],t[3],byref(t[4]),byref(t[5]))
    return (r,source,srcscale,position,mult,float(t[4].value),float(t[5].value))
     
def RPR_GetTempoTimeSigMarker(proj,ptidx,timeposOut,measureposOut,beatposOut,bpmOut,timesig_numOut,timesig_denomOut,lineartempoOut):
    """
    Python: (Boolean retval, ReaProject proj, Int ptidx, Float timeposOut, Int measureposOut, Float beatposOut, Float bpmOut, Int timesig_numOut, Int timesig_denomOut, Boolean lineartempoOut) = RPR_GetTempoTimeSigMarker(proj, ptidx, timeposOut, measureposOut, beatposOut, bpmOut, timesig_numOut, timesig_denomOut, lineartempoOut)
    
    Get information about a tempo/time signature marker. See CountTempoTimeSigMarkers
    , SetTempoTimeSigMarker
    , AddTempoTimeSigMarker
    .
    """
    a=_ft['GetTempoTimeSigMarker']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(ptidx),c_double(timeposOut),c_int(measureposOut),c_double(beatposOut),c_double(bpmOut),c_int(timesig_numOut),c_int(timesig_denomOut),c_byte(lineartempoOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]))
    return (r,proj,ptidx,float(t[2].value),int(t[3].value),float(t[4].value),float(t[5].value),int(t[6].value),int(t[7].value),int(t[8].value))
     
def RPR_GetToggleCommandState(command_id):
    """
    Python: Int  RPR_GetToggleCommandState(Int command_id)
    
    See GetToggleCommandStateEx
    .
    """
    a=_ft['GetToggleCommandState']
    f=CFUNCTYPE(c_int,c_int)(a)
    t=(c_int(command_id),)
    r=f(t[0])
    return r
     
def RPR_GetToggleCommandStateEx(section_id,command_id):
    """
    Python: Int  RPR_GetToggleCommandStateEx(Int section_id, Int command_id)
    
    For the main action context, the MIDI editor, or the media explorer, returns the toggle state of the action. 0=off, 1=on, -1=NA because the action does not have on/off states. For the MIDI editor, the action state for the most recently focused window will be returned.
    """
    a=_ft['GetToggleCommandStateEx']
    f=CFUNCTYPE(c_int,c_int,c_int)(a)
    t=(c_int(section_id),c_int(command_id))
    r=f(t[0],t[1])
    return r
     
def RPR_GetTooltipWindow():
    """
    Python: HWND  RPR_GetTooltipWindow()
    
    gets a tooltip window,in case you want to ask it for font information. Can return NULL.
    """
    a=_ft['GetTooltipWindow']
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('HWND',r)
     
def RPR_GetTrack(proj,trackidx):
    """
    Python: MediaTrack  RPR_GetTrack(ReaProject proj, Int trackidx)
    
    get a track from a project by track count (zero-based) (proj=0 for active project)
    """
    a=_ft['GetTrack']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(trackidx))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_GetTrackAutomationMode(tr):
    """
    Python: Int  RPR_GetTrackAutomationMode(MediaTrack tr)
    
    return the track mode, regardless of global override
    """
    a=_ft['GetTrackAutomationMode']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),)
    r=f(t[0])
    return r
     
def RPR_GetTrackColor(track):
    """
    Python: Int  RPR_GetTrackColor(MediaTrack track)
    
    Returns the track custom color as OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). Black is returned as 0x01000000, no color setting is returned as 0.
    """
    a=_ft['GetTrackColor']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_GetTrackDepth(track):
    """
    Python: Int  RPR_GetTrackDepth(MediaTrack track)
    """
    a=_ft['GetTrackDepth']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_GetTrackEnvelope(track,envidx):
    """
    Python: TrackEnvelope  RPR_GetTrackEnvelope(MediaTrack track, Int envidx)
    """
    a=_ft['GetTrackEnvelope']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(envidx))
    r=f(t[0],t[1])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetTrackEnvelopeByChunkName(tr,cfgchunkname):
    """
    Python: TrackEnvelope  RPR_GetTrackEnvelopeByChunkName(MediaTrack tr, String cfgchunkname)
    
    Gets a built-in track envelope by configuration chunk name, e.g. "<VOLENV".
    """
    a=_ft['GetTrackEnvelopeByChunkName']
    f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packsc(cfgchunkname))
    r=f(t[0],t[1])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetTrackEnvelopeByName(track,envname):
    """
    Python: TrackEnvelope  RPR_GetTrackEnvelopeByName(MediaTrack track, String envname)
    """
    a=_ft['GetTrackEnvelopeByName']
    f=CFUNCTYPE(c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packsc(envname))
    r=f(t[0],t[1])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_GetTrackGUID(tr):
    """
    Python: GUID  RPR_GetTrackGUID(MediaTrack tr)
    """
    a=_ft['GetTrackGUID']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),)
    r=f(t[0])
    return rpr_unpackp('GUID*',r)
     
def RPR_GetTrackMediaItem(tr,itemidx):
    """
    Python: MediaItem  RPR_GetTrackMediaItem(MediaTrack tr, Int itemidx)
    """
    a=_ft['GetTrackMediaItem']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(itemidx))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem*',r)
     
def RPR_GetTrackMIDILyrics(track,flag,bufWant16384,bufWant16384_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int flag, String bufWant16384, Int bufWant16384_sz) = RPR_GetTrackMIDILyrics(track, flag, bufWant16384, bufWant16384_sz)
    
    Get all MIDI lyrics on the track. Lyrics will be returned as one string with tabs between each word. flag&1: double tabs at the end of each measure and triple tabs when skipping measures, flag&2: each lyric is preceded by its beat position in the project (example with flag=2: "1.1.2\tLyric for measure 1 beat 2\t.1.1\tLyric for measure 2 beat 1	"). See SetTrackMIDILyrics
    """
    a=_ft['GetTrackMIDILyrics']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(flag),rpr_packs(bufWant16384),c_int(bufWant16384_sz))
    r=f(t[0],t[1],t[2],byref(t[3]))
    return (r,track,flag,rpr_unpacks(t[2]),int(t[3].value))
     
def RPR_GetTrackMIDINoteName(track,pitch,chan):
    """
    Python: String  RPR_GetTrackMIDINoteName(Int track, Int pitch, Int chan)
    
    see GetTrackMIDINoteNameEx
    """
    a=_ft['GetTrackMIDINoteName']
    f=CFUNCTYPE(c_char_p,c_int,c_int,c_int)(a)
    t=(c_int(track),c_int(pitch),c_int(chan))
    r=f(t[0],t[1],t[2])
    return str(r.decode())
     
def RPR_GetTrackMIDINoteNameEx(proj,track,pitch,chan):
    """
    Python: String  RPR_GetTrackMIDINoteNameEx(ReaProject proj, MediaTrack track, Int pitch, Int chan)
    
    Get note/CC name. pitch 128 for CC0 name, 129 for CC1 name, etc. See SetTrackMIDINoteNameEx
    """
    a=_ft['GetTrackMIDINoteNameEx']
    f=CFUNCTYPE(c_char_p,c_uint64,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packp('MediaTrack*',track),c_int(pitch),c_int(chan))
    r=f(t[0],t[1],t[2],t[3])
    return str(r.decode())
     
def RPR_GetTrackMIDINoteRange(proj,track,note_loOut,note_hiOut):
    """
    Python: (ReaProject proj, MediaTrack track, Int note_loOut, Int note_hiOut) = RPR_GetTrackMIDINoteRange(proj, track, note_loOut, note_hiOut)
    """
    a=_ft['GetTrackMIDINoteRange']
    f=CFUNCTYPE(None,c_uint64,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packp('MediaTrack*',track),c_int(note_loOut),c_int(note_hiOut))
    f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (proj,track,int(t[2].value),int(t[3].value))
     
def RPR_GetTrackName(track,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, String buf, Int buf_sz) = RPR_GetTrackName(track, buf, buf_sz)
    
    Returns "MASTER" for master track, "Track N" if track has no name.
    """
    a=_ft['GetTrackName']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2])
    return (r,track,rpr_unpacks(t[1]),buf_sz)
     
def RPR_GetTrackNumMediaItems(tr):
    """
    Python: Int  RPR_GetTrackNumMediaItems(MediaTrack tr)
    """
    a=_ft['GetTrackNumMediaItems']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',tr),)
    r=f(t[0])
    return r
     
def RPR_GetTrackNumSends(tr,category):
    """
    Python: Int  RPR_GetTrackNumSends(MediaTrack tr, Int category)
    
    returns number of sends/receives/hardware outputs - category is <0 for receives, 0=sends, >0 for hardware outputs
    """
    a=_ft['GetTrackNumSends']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(category))
    r=f(t[0],t[1])
    return r
     
def RPR_GetTrackReceiveName(track,recv_index,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int recv_index, String buf, Int buf_sz) = RPR_GetTrackReceiveName(track, recv_index, buf, buf_sz)
    
    See GetTrackSendName
    .
    """
    a=_ft['GetTrackReceiveName']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(recv_index),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,recv_index,rpr_unpacks(t[2]),buf_sz)
     
def RPR_GetTrackReceiveUIMute(track,recv_index,muteOut):
    """
    Python: (Boolean retval, MediaTrack track, Int recv_index, Boolean muteOut) = RPR_GetTrackReceiveUIMute(track, recv_index, muteOut)
    
    See GetTrackSendUIMute
    .
    """
    a=_ft['GetTrackReceiveUIMute']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(recv_index),c_byte(muteOut))
    r=f(t[0],t[1],byref(t[2]))
    return (r,track,recv_index,int(t[2].value))
     
def RPR_GetTrackReceiveUIVolPan(track,recv_index,volumeOut,panOut):
    """
    Python: (Boolean retval, MediaTrack track, Int recv_index, Float volumeOut, Float panOut) = RPR_GetTrackReceiveUIVolPan(track, recv_index, volumeOut, panOut)
    
    See GetTrackSendUIVolPan
    .
    """
    a=_ft['GetTrackReceiveUIVolPan']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(recv_index),c_double(volumeOut),c_double(panOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (r,track,recv_index,float(t[2].value),float(t[3].value))
     
def RPR_GetTrackSendInfo_Value(tr,category,sendidx,parmname):
    """
    Python: Float  RPR_GetTrackSendInfo_Value(MediaTrack tr, Int category, Int sendidx, String parmname)
    
    Get send/receive/hardware output numerical-value attributes.
    
    category is <0 for receives, 0=sends, >0 for hardware outputs
    
    parameter names:
    
    B_MUTE : returns bool *
    
    B_PHASE : returns bool *, true to flip phase
    
    B_MONO : returns bool *
    
    D_VOL : returns double *, 1.0 = +0dB etc
    
    D_PAN : returns double *, -1..+1
    
    D_PANLAW : returns double *,1.0=+0.0db, 0.5=-6dB, -1.0 = projdef etc
    
    I_SENDMODE : returns int *, 0=post-fader, 1=pre-fx, 2=post-fx (deprecated), 3=post-fx
    
    I_AUTOMODE : returns int * : automation mode (-1=use track automode, 0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
    
    I_SRCCHAN : returns int *, index,&1024=mono, -1 for none
    
    I_DSTCHAN : returns int *, index, &1024=mono, otherwise stereo pair, hwout:&512=rearoute
    
    I_MIDIFLAGS : returns int *, low 5 bits=source channel 0=all, 1-16, next 5 bits=dest channel, 0=orig, 1-16=chanP_DESTTRACK : read only, returns MediaTrack *, destination track, only applies for sends/recvs
    
    P_SRCTRACK : read only, returns MediaTrack *, source track, only applies for sends/recvs
    
    P_ENV : read only, returns TrackEnvelope *, setNewValue=<VOLENV, <PANENV, etc
    
    See CreateTrackSend
    , RemoveTrackSend
    , GetTrackNumSends
    .
    """
    a=_ft['GetTrackSendInfo_Value']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(category),c_int(sendidx),rpr_packsc(parmname))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_GetTrackSendName(track,send_index,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int send_index, String buf, Int buf_sz) = RPR_GetTrackSendName(track, send_index, buf, buf_sz)
    
    send_idx>=0 for hw ouputs, >=nb_of_hw_ouputs for sends. See GetTrackReceiveName
    .
    """
    a=_ft['GetTrackSendName']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(send_index),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,send_index,rpr_unpacks(t[2]),buf_sz)
     
def RPR_GetTrackSendUIMute(track,send_index,muteOut):
    """
    Python: (Boolean retval, MediaTrack track, Int send_index, Boolean muteOut) = RPR_GetTrackSendUIMute(track, send_index, muteOut)
    
    send_idx>=0 for hw ouputs, >=nb_of_hw_ouputs for sends. See GetTrackReceiveUIMute
    .
    """
    a=_ft['GetTrackSendUIMute']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(send_index),c_byte(muteOut))
    r=f(t[0],t[1],byref(t[2]))
    return (r,track,send_index,int(t[2].value))
     
def RPR_GetTrackSendUIVolPan(track,send_index,volumeOut,panOut):
    """
    Python: (Boolean retval, MediaTrack track, Int send_index, Float volumeOut, Float panOut) = RPR_GetTrackSendUIVolPan(track, send_index, volumeOut, panOut)
    
    send_idx>=0 for hw ouputs, >=nb_of_hw_ouputs for sends. See GetTrackReceiveUIVolPan
    .
    """
    a=_ft['GetTrackSendUIVolPan']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(send_index),c_double(volumeOut),c_double(panOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (r,track,send_index,float(t[2].value),float(t[3].value))
     
def RPR_GetTrackState(track,flagsOut):
    """
    Python: (String retval, MediaTrack track, Int flagsOut) = RPR_GetTrackState(track, flagsOut)
    
    Gets track state, returns track name.
    
    flags will be set to:
    
    &1=folder
    
    &2=selected
    
    &4=has fx enabled
    
    &8=muted
    
    &16=soloed
    
    &32=SIP'd (with &16)
    
    &64=rec armed
    
    &128=rec monitoring on
    
    &256=rec monitoring auto
    
    &512=hide from TCP
    
    &1024=hide from MCP
    """
    a=_ft['GetTrackState']
    f=CFUNCTYPE(c_char_p,c_uint64,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(flagsOut))
    r=f(t[0],byref(t[1]))
    return (str(r.decode()),track,int(t[1].value))
     
def RPR_GetTrackStateChunk(track,strNeedBig,strNeedBig_sz,isundoOptional):
    """
    Python: (Boolean retval, MediaTrack track, String strNeedBig, Int strNeedBig_sz, Boolean isundoOptional) = RPR_GetTrackStateChunk(track, strNeedBig, strNeedBig_sz, isundoOptional)
    
    Gets the RPPXML state of a track, returns true if successful. Undo flag is a performance/caching hint.
    """
    a=_ft['GetTrackStateChunk']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packs(strNeedBig),c_int(strNeedBig_sz),c_byte(isundoOptional))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,rpr_unpacks(t[1]),strNeedBig_sz,isundoOptional)
     
def RPR_GetTrackUIMute(track,muteOut):
    """
    Python: (Boolean retval, MediaTrack track, Boolean muteOut) = RPR_GetTrackUIMute(track, muteOut)
    """
    a=_ft['GetTrackUIMute']
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_byte(muteOut))
    r=f(t[0],byref(t[1]))
    return (r,track,int(t[1].value))
     
def RPR_GetTrackUIPan(track,pan1Out,pan2Out,panmodeOut):
    """
    Python: (Boolean retval, MediaTrack track, Float pan1Out, Float pan2Out, Int panmodeOut) = RPR_GetTrackUIPan(track, pan1Out, pan2Out, panmodeOut)
    """
    a=_ft['GetTrackUIPan']
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_double(pan1Out),c_double(pan2Out),c_int(panmodeOut))
    r=f(t[0],byref(t[1]),byref(t[2]),byref(t[3]))
    return (r,track,float(t[1].value),float(t[2].value),int(t[3].value))
     
def RPR_GetTrackUIVolPan(track,volumeOut,panOut):
    """
    Python: (Boolean retval, MediaTrack track, Float volumeOut, Float panOut) = RPR_GetTrackUIVolPan(track, volumeOut, panOut)
    """
    a=_ft['GetTrackUIVolPan']
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_double(volumeOut),c_double(panOut))
    r=f(t[0],byref(t[1]),byref(t[2]))
    return (r,track,float(t[1].value),float(t[2].value))
     
def RPR_GetUnderrunTime(audio_xrunOutOptional,media_xrunOutOptional,curtimeOutOptional):
    """
    Python: RPR_GetUnderrunTime(unsigned int audio_xrunOutOptional, unsigned int media_xrunOutOptional, unsigned int curtimeOutOptional)
    
    retrieves the last timestamps of audio xrun (yellow-flash, if available), media xrun (red-flash), and the current time stamp (all milliseconds)
    """
    a=_ft['GetUnderrunTime']
    f=CFUNCTYPE(None,c_void_p,c_void_p,c_void_p)(a)
    t=(c_int(audio_xrunOutOptional),c_int(media_xrunOutOptional),c_int(curtimeOutOptional))
    f(byref(t[0]),byref(t[1]),byref(t[2]))
    return (int(t[0].value),int(t[1].value),int(t[2].value))
     
def RPR_GetUserFileNameForRead(filenameNeed4096,title,defext):
    """
    Python: (Boolean retval, String filenameNeed4096, String title, String defext) = RPR_GetUserFileNameForRead(filenameNeed4096, title, defext)
    
    returns true if the user selected a valid file, false if the user canceled the dialog
    """
    a=_ft['GetUserFileNameForRead']
    f=CFUNCTYPE(c_byte,c_char_p,c_char_p,c_char_p)(a)
    t=(rpr_packs(filenameNeed4096),rpr_packsc(title),rpr_packsc(defext))
    r=f(t[0],t[1],t[2])
    return (r,rpr_unpacks(t[0]),title,defext)
     
def RPR_GetUserInputs(title,num_inputs,captions_csv,retvals_csv,retvals_csv_sz):
    """
    Python: (Boolean retval, String title, Int num_inputs, String captions_csv, String retvals_csv, Int retvals_csv_sz) = RPR_GetUserInputs(title, num_inputs, captions_csv, retvals_csv, retvals_csv_sz)
    
    Get values from the user.
    
    If a caption begins with *, for example "*password", the edit field will not display the input text.
    
    Maximum fields is 16. Values are returned as a comma-separated string. Returns false if the user canceled the dialog. To increase text field width, add an extra caption field, and specify extrawidth=xyz
    """
    a=_ft['GetUserInputs']
    f=CFUNCTYPE(c_byte,c_char_p,c_int,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(title),c_int(num_inputs),rpr_packsc(captions_csv),rpr_packs(retvals_csv),c_int(retvals_csv_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,title,num_inputs,captions_csv,rpr_unpacks(t[3]),retvals_csv_sz)
     
def RPR_GoToMarker(proj,marker_index,use_timeline_order):
    """
    Python: RPR_GoToMarker(ReaProject proj, Int marker_index, Boolean use_timeline_order)
    
    Go to marker. If use_timeline_order==true, marker_index 1 refers to the first marker on the timeline.  If use_timeline_order==false, marker_index 1 refers to the first marker with the user-editable index of 1.
    """
    a=_ft['GoToMarker']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(marker_index),c_byte(use_timeline_order))
    f(t[0],t[1],t[2])
     
def RPR_GoToRegion(proj,region_index,use_timeline_order):
    """
    Python: RPR_GoToRegion(ReaProject proj, Int region_index, Boolean use_timeline_order)
    
    Seek to region after current region finishes playing (smooth seek). If use_timeline_order==true, region_index 1 refers to the first region on the timeline.  If use_timeline_order==false, region_index 1 refers to the first region with the user-editable index of 1.
    """
    a=_ft['GoToRegion']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(region_index),c_byte(use_timeline_order))
    f(t[0],t[1],t[2])
     
def RPR_GR_SelectColor(hwnd,colorOut):
    """
    Python: (Int retval, HWND hwnd, Int colorOut) = RPR_GR_SelectColor(hwnd, colorOut)
    
    Runs the system color chooser dialog.  Returns 0 if the user cancels the dialog.
    """
    a=_ft['GR_SelectColor']
    f=CFUNCTYPE(c_int,c_uint64,c_void_p)(a)
    t=(rpr_packp('HWND',hwnd),c_int(colorOut))
    r=f(t[0],byref(t[1]))
    return (r,hwnd,int(t[1].value))
     
def RPR_GSC_mainwnd(t):
    """
    Python: Int  RPR_GSC_mainwnd(Int t)
    
    this is just like win32 GetSysColor() but can have overrides.
    """
    a=_ft['GSC_mainwnd']
    f=CFUNCTYPE(c_int,c_int)(a)
    t=(c_int(t),)
    r=f(t[0])
    return r
     
def RPR_guidToString(g,destNeed64):
    """
    Python: (const GUID g, String destNeed64) = RPR_guidToString(g, destNeed64)
    
    dest should be at least 64 chars long to be safe
    """
    a=_ft['guidToString']
    f=CFUNCTYPE(None,c_uint64,c_char_p)(a)
    t=(rpr_packp('GUID*',g),rpr_packs(destNeed64))
    f(t[0],t[1])
    return (g,rpr_unpacks(t[1]))
     
def RPR_HasExtState(section,key):
    """
    Python: Boolean  RPR_HasExtState(String section, String key)
    
    Returns true if there exists an extended state value for a specific section and key. See SetExtState
    , GetExtState
    , DeleteExtState
    .
    """
    a=_ft['HasExtState']
    f=CFUNCTYPE(c_byte,c_char_p,c_char_p)(a)
    t=(rpr_packsc(section),rpr_packsc(key))
    r=f(t[0],t[1])
    return r
     
def RPR_HasTrackMIDIPrograms(track):
    """
    Python: String  RPR_HasTrackMIDIPrograms(Int track)
    
    returns name of track plugin that is supplying MIDI programs,or NULL if there is none
    """
    a=_ft['HasTrackMIDIPrograms']
    f=CFUNCTYPE(c_char_p,c_int)(a)
    t=(c_int(track),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_HasTrackMIDIProgramsEx(proj,track):
    """
    Python: String  RPR_HasTrackMIDIProgramsEx(ReaProject proj, MediaTrack track)
    
    returns name of track plugin that is supplying MIDI programs,or NULL if there is none
    """
    a=_ft['HasTrackMIDIProgramsEx']
    f=CFUNCTYPE(c_char_p,c_uint64,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packp('MediaTrack*',track))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_Help_Set(helpstring,is_temporary_help):
    """
    Python: RPR_Help_Set(String helpstring, Boolean is_temporary_help)
    """
    a=_ft['Help_Set']
    f=CFUNCTYPE(None,c_char_p,c_byte)(a)
    t=(rpr_packsc(helpstring),c_byte(is_temporary_help))
    f(t[0],t[1])
     
def RPR_image_resolve_fn(In,out,out_sz):
    """
    Python: (String in, String out, Int out_sz) = RPR_image_resolve_fn(in, out, out_sz)
    """
    a=_ft['image_resolve_fn']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(In),rpr_packs(out),c_int(out_sz))
    f(t[0],t[1],t[2])
    return (In,rpr_unpacks(t[1]),out_sz)
     
def RPR_InsertAutomationItem(env,pool_id,position,length):
    """
    Python: Int  RPR_InsertAutomationItem(TrackEnvelope env, Int pool_id, Float position, Float length)
    
    Insert a new automation item. pool_id < 0 collects existing envelope points into the automation item; otherwise, the automation item will be a new instance of an existing pool. Returns the index of the item, suitable for passing to other automation item API functions. See GetSetAutomationItemInfo
    .
    """
    a=_ft['InsertAutomationItem']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_double,c_double)(a)
    t=(rpr_packp('TrackEnvelope*',env),c_int(pool_id),c_double(position),c_double(length))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_InsertEnvelopePoint(envelope,time,value,shape,tension,selected,noSortInOptional):
    """
    Python: (Boolean retval, TrackEnvelope envelope, Float time, Float value, Int shape, Float tension, Boolean selected, Boolean noSortInOptional) = RPR_InsertEnvelopePoint(envelope, time, value, shape, tension, selected, noSortInOptional)
    
    Insert an envelope point. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done. See GetEnvelopePoint
    , SetEnvelopePoint
    , GetEnvelopeScalingMode
    .
    """
    a=_ft['InsertEnvelopePoint']
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_double,c_int,c_double,c_byte,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_double(time),c_double(value),c_int(shape),c_double(tension),c_byte(selected),c_byte(noSortInOptional))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],byref(t[6]))
    return (r,envelope,time,value,shape,tension,selected,int(t[6].value))
     
def RPR_InsertEnvelopePointEx(envelope,autoitem_idx,time,value,shape,tension,selected,noSortInOptional):
    """
    Python: (Boolean retval, TrackEnvelope envelope, Int autoitem_idx, Float time, Float value, Int shape, Float tension, Boolean selected, Boolean noSortInOptional) = RPR_InsertEnvelopePointEx(envelope, autoitem_idx, time, value, shape, tension, selected, noSortInOptional)
    
    Insert an envelope point. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePoint
    , SetEnvelopePoint
    , GetEnvelopeScalingMode
    .
    """
    a=_ft['InsertEnvelopePointEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double,c_double,c_int,c_double,c_byte,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(autoitem_idx),c_double(time),c_double(value),c_int(shape),c_double(tension),c_byte(selected),c_byte(noSortInOptional))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],byref(t[7]))
    return (r,envelope,autoitem_idx,time,value,shape,tension,selected,int(t[7].value))
     
def RPR_InsertMedia(file,mode):
    """
    Python: Int  RPR_InsertMedia(String file, Int mode)
    
    mode: 0=add to current track, 1=add new track, 3=add to selected items as takes, &4=stretch/loop to fit time sel, &8=try to match tempo 1x, &16=try to match tempo 0.5x, &32=try to match tempo 2x, &64=don't preserve pitch when matching tempo, &128=no loop/section if startpct/endpct set, &256=force loop regardless of global preference for looping imported items. &512=use high word as absolute track index if mode&3==0.
    """
    a=_ft['InsertMedia']
    f=CFUNCTYPE(c_int,c_char_p,c_int)(a)
    t=(rpr_packsc(file),c_int(mode))
    r=f(t[0],t[1])
    return r
     
def RPR_InsertMediaSection(file,mode,startpct,endpct,pitchshift):
    """
    Python: Int  RPR_InsertMediaSection(String file, Int mode, Float startpct, Float endpct, Float pitchshift)
    """
    a=_ft['InsertMediaSection']
    f=CFUNCTYPE(c_int,c_char_p,c_int,c_double,c_double,c_double)(a)
    t=(rpr_packsc(file),c_int(mode),c_double(startpct),c_double(endpct),c_double(pitchshift))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def RPR_InsertTrackAtIndex(idx,wantDefaults):
    """
    Python: RPR_InsertTrackAtIndex(Int idx, Boolean wantDefaults)
    
    inserts a track at idx,of course this will be clamped to 0..GetNumTracks(). wantDefaults=TRUE for default envelopes/FX,otherwise no enabled fx/env
    """
    a=_ft['InsertTrackAtIndex']
    f=CFUNCTYPE(None,c_int,c_byte)(a)
    t=(c_int(idx),c_byte(wantDefaults))
    f(t[0],t[1])
     
def RPR_IsMediaExtension(ext,wantOthers):
    """
    Python: Boolean  RPR_IsMediaExtension(String ext, Boolean wantOthers)
    
    Tests a file extension (i.e. "wav" or "mid") to see if it's a media extension.
    
    If wantOthers is set, then "RPP", "TXT" and other project-type formats will also pass.
    """
    a=_ft['IsMediaExtension']
    f=CFUNCTYPE(c_byte,c_char_p,c_byte)(a)
    t=(rpr_packsc(ext),c_byte(wantOthers))
    r=f(t[0],t[1])
    return r
     
def RPR_IsMediaItemSelected(item):
    """
    Python: Boolean  RPR_IsMediaItemSelected(MediaItem item)
    """
    a=_ft['IsMediaItemSelected']
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    r=f(t[0])
    return r
     
def RPR_IsProjectDirty(proj):
    """
    Python: Int  RPR_IsProjectDirty(ReaProject proj)
    
    Is the project dirty (needing save)? Always returns 0 if 'undo/prompt to save' is disabled in preferences.
    """
    a=_ft['IsProjectDirty']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_IsTrackSelected(track):
    """
    Python: Boolean  RPR_IsTrackSelected(MediaTrack track)
    """
    a=_ft['IsTrackSelected']
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_IsTrackVisible(track,mixer):
    """
    Python: Boolean  RPR_IsTrackVisible(MediaTrack track, Boolean mixer)
    
    If mixer==true, returns true if the track is visible in the mixer.  If mixer==false, returns true if the track is visible in the track control panel.
    """
    a=_ft['IsTrackVisible']
    f=CFUNCTYPE(c_byte,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_byte(mixer))
    r=f(t[0],t[1])
    return r
     
def RPR_joystick_create(guid):
    """
    Python: joystick_device  RPR_joystick_create(const GUID guid)
    
    creates a joystick device
    """
    a=_ft['joystick_create']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('GUID*',guid),)
    r=f(t[0])
    return rpr_unpackp('joystick_device*',r)
     
def RPR_joystick_destroy(device):
    """
    Python: RPR_joystick_destroy(joystick_device device)
    
    destroys a joystick device
    """
    a=_ft['joystick_destroy']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('joystick_device*',device),)
    f(t[0])
     
def RPR_joystick_enum(index,namestrOutOptional):
    """
    Python: String  RPR_joystick_enum(Int index, String namestrOutOptional)
    
    enumerates installed devices, returns GUID as a string
    """
    a=_ft['joystick_enum']
    f=CFUNCTYPE(c_char_p,c_int,c_uint64)(a)
    t=(c_int(index),rpr_packp('char**',namestrOutOptional))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_joystick_getaxis(dev,axis):
    """
    Python: Float  RPR_joystick_getaxis(joystick_device dev, Int axis)
    
    returns axis value (-1..1)
    """
    a=_ft['joystick_getaxis']
    f=CFUNCTYPE(c_double,c_uint64,c_int)(a)
    t=(rpr_packp('joystick_device*',dev),c_int(axis))
    r=f(t[0],t[1])
    return r
     
def RPR_joystick_getbuttonmask(dev):
    """
    Python: Unknown  RPR_joystick_getbuttonmask(joystick_device dev)
    
    returns button pressed mask, 1=first button, 2=second...
    """
    a=_ft['joystick_getbuttonmask']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('joystick_device*',dev),)
    r=f(t[0])
    return r
     
def RPR_joystick_getinfo(dev,axesOutOptional,povsOutOptional):
    """
    Python: (Int retval, joystick_device dev, Int axesOutOptional, Int povsOutOptional) = RPR_joystick_getinfo(dev, axesOutOptional, povsOutOptional)
    
    returns button count
    """
    a=_ft['joystick_getinfo']
    f=CFUNCTYPE(c_int,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('joystick_device*',dev),c_int(axesOutOptional),c_int(povsOutOptional))
    r=f(t[0],byref(t[1]),byref(t[2]))
    return (r,dev,int(t[1].value),int(t[2].value))
     
def RPR_joystick_getpov(dev,pov):
    """
    Python: Float  RPR_joystick_getpov(joystick_device dev, Int pov)
    
    returns POV value (usually 0..655.35, or 655.35 on error)
    """
    a=_ft['joystick_getpov']
    f=CFUNCTYPE(c_double,c_uint64,c_int)(a)
    t=(rpr_packp('joystick_device*',dev),c_int(pov))
    r=f(t[0],t[1])
    return r
     
def RPR_joystick_update(dev):
    """
    Python: Boolean  RPR_joystick_update(joystick_device dev)
    
    Updates joystick state from hardware, returns true if successful (joystick_get* will not be valid until joystick_update() is called successfully)
    """
    a=_ft['joystick_update']
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('joystick_device*',dev),)
    r=f(t[0])
    return r
     
def RPR_LICE_ClipLine(pX1Out,pY1Out,pX2Out,pY2Out,xLo,yLo,xHi,yHi):
    """
    Python: (Boolean retval, Int pX1Out, Int pY1Out, Int pX2Out, Int pY2Out, Int xLo, Int yLo, Int xHi, Int yHi) = RPR_LICE_ClipLine(pX1Out, pY1Out, pX2Out, pY2Out, xLo, yLo, xHi, yHi)
    
    Returns false if the line is entirely offscreen.
    """
    a=_ft['LICE_ClipLine']
    f=CFUNCTYPE(c_byte,c_void_p,c_void_p,c_void_p,c_void_p,c_int,c_int,c_int,c_int)(a)
    t=(c_int(pX1Out),c_int(pY1Out),c_int(pX2Out),c_int(pY2Out),c_int(xLo),c_int(yLo),c_int(xHi),c_int(yHi))
    r=f(byref(t[0]),byref(t[1]),byref(t[2]),byref(t[3]),t[4],t[5],t[6],t[7])
    return (r,int(t[0].value),int(t[1].value),int(t[2].value),int(t[3].value),xLo,yLo,xHi,yHi)
     
def RPR_Loop_OnArrow(project,direction):
    """
    Python: Boolean  RPR_Loop_OnArrow(ReaProject project, Int direction)
    
    Move the loop selection left or right. Returns true if snap is enabled.
    """
    a=_ft['Loop_OnArrow']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',project),c_int(direction))
    r=f(t[0],t[1])
    return r
     
def RPR_Main_OnCommand(command,flag):
    """
    Python: RPR_Main_OnCommand(Int command, Int flag)
    
    See Main_OnCommandEx
    .
    """
    a=_ft['Main_OnCommand']
    f=CFUNCTYPE(None,c_int,c_int)(a)
    t=(c_int(command),c_int(flag))
    f(t[0],t[1])
     
def RPR_Main_OnCommandEx(command,flag,proj):
    """
    Python: RPR_Main_OnCommandEx(Int command, Int flag, ReaProject proj)
    
    Performs an action belonging to the main action section. To perform non-native actions (ReaScripts, custom or extension plugins' actions) safely, see NamedCommandLookup
    ().
    """
    a=_ft['Main_OnCommandEx']
    f=CFUNCTYPE(None,c_int,c_int,c_uint64)(a)
    t=(c_int(command),c_int(flag),rpr_packp('ReaProject*',proj))
    f(t[0],t[1],t[2])
     
def RPR_Main_openProject(name):
    """
    Python: RPR_Main_openProject(String name)
    
    opens a project. will prompt the user to save, etc.
    
    if you pass a .RTrackTemplate file then it adds that to the project instead.
    """
    a=_ft['Main_openProject']
    f=CFUNCTYPE(None,c_char_p)(a)
    t=(rpr_packsc(name),)
    f(t[0])
     
def RPR_Main_SaveProject(proj,forceSaveAsInOptional):
    """
    Python: RPR_Main_SaveProject(ReaProject proj, Boolean forceSaveAsInOptional)
    
    Save the project.
    """
    a=_ft['Main_SaveProject']
    f=CFUNCTYPE(None,c_uint64,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(forceSaveAsInOptional))
    f(t[0],t[1])
     
def RPR_Main_UpdateLoopInfo(ignoremask):
    """
    Python: RPR_Main_UpdateLoopInfo(Int ignoremask)
    """
    a=_ft['Main_UpdateLoopInfo']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(ignoremask),)
    f(t[0])
     
def RPR_MarkProjectDirty(proj):
    """
    Python: RPR_MarkProjectDirty(ReaProject proj)
    
    Marks project as dirty (needing save) if 'undo/prompt to save' is enabled in preferences.
    """
    a=_ft['MarkProjectDirty']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    f(t[0])
     
def RPR_MarkTrackItemsDirty(track,item):
    """
    Python: RPR_MarkTrackItemsDirty(MediaTrack track, MediaItem item)
    
    If track is supplied, item is ignored
    """
    a=_ft['MarkTrackItemsDirty']
    f=CFUNCTYPE(None,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packp('MediaItem*',item))
    f(t[0],t[1])
     
def RPR_Master_GetPlayRate(project):
    """
    Python: Float  RPR_Master_GetPlayRate(ReaProject project)
    """
    a=_ft['Master_GetPlayRate']
    f=CFUNCTYPE(c_double,c_uint64)(a)
    t=(rpr_packp('ReaProject*',project),)
    r=f(t[0])
    return r
     
def RPR_Master_GetPlayRateAtTime(time_s,proj):
    """
    Python: Float  RPR_Master_GetPlayRateAtTime(Float time_s, ReaProject proj)
    """
    a=_ft['Master_GetPlayRateAtTime']
    f=CFUNCTYPE(c_double,c_double,c_uint64)(a)
    t=(c_double(time_s),rpr_packp('ReaProject*',proj))
    r=f(t[0],t[1])
    return r
     
def RPR_Master_GetTempo():
    """
    Python: Float  RPR_Master_GetTempo()
    """
    a=_ft['Master_GetTempo']
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def RPR_Master_NormalizePlayRate(playrate,isnormalized):
    """
    Python: Float  RPR_Master_NormalizePlayRate(Float playrate, Boolean isnormalized)
    
    Convert play rate to/from a value between 0 and 1, representing the position on the project playrate slider.
    """
    a=_ft['Master_NormalizePlayRate']
    f=CFUNCTYPE(c_double,c_double,c_byte)(a)
    t=(c_double(playrate),c_byte(isnormalized))
    r=f(t[0],t[1])
    return r
     
def RPR_Master_NormalizeTempo(bpm,isnormalized):
    """
    Python: Float  RPR_Master_NormalizeTempo(Float bpm, Boolean isnormalized)
    
    Convert the tempo to/from a value between 0 and 1, representing bpm in the range of 40-296 bpm.
    """
    a=_ft['Master_NormalizeTempo']
    f=CFUNCTYPE(c_double,c_double,c_byte)(a)
    t=(c_double(bpm),c_byte(isnormalized))
    r=f(t[0],t[1])
    return r
     
def RPR_MB(msg,title,Type):
    """
    Python: Int  RPR_MB(String msg, String title, Int type)
    
    type 0=OK,1=OKCANCEL,2=ABORTRETRYIGNORE,3=YESNOCANCEL,4=YESNO,5=RETRYCANCEL : ret 1=OK,2=CANCEL,3=ABORT,4=RETRY,5=IGNORE,6=YES,7=NO
    """
    a=_ft['MB']
    f=CFUNCTYPE(c_int,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(msg),rpr_packsc(title),c_int(Type))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_MediaItemDescendsFromTrack(item,track):
    """
    Python: Int  RPR_MediaItemDescendsFromTrack(MediaItem item, MediaTrack track)
    
    Returns 1 if the track holds the item, 2 if the track is a folder containing the track that holds the item, etc.
    """
    a=_ft['MediaItemDescendsFromTrack']
    f=CFUNCTYPE(c_int,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packp('MediaTrack*',track))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_CountEvts(take,notecntOut,ccevtcntOut,textsyxevtcntOut):
    """
    Python: (Int retval, MediaItem_Take take, Int notecntOut, Int ccevtcntOut, Int textsyxevtcntOut) = RPR_MIDI_CountEvts(take, notecntOut, ccevtcntOut, textsyxevtcntOut)
    
    Count the number of notes, CC events, and text/sysex events in a given MIDI item.
    """
    a=_ft['MIDI_CountEvts']
    f=CFUNCTYPE(c_int,c_uint64,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(notecntOut),c_int(ccevtcntOut),c_int(textsyxevtcntOut))
    r=f(t[0],byref(t[1]),byref(t[2]),byref(t[3]))
    return (r,take,int(t[1].value),int(t[2].value),int(t[3].value))
     
def RPR_MIDI_DeleteCC(take,ccidx):
    """
    Python: Boolean  RPR_MIDI_DeleteCC(MediaItem_Take take, Int ccidx)
    
    Delete a MIDI CC event.
    """
    a=_ft['MIDI_DeleteCC']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(ccidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_DeleteEvt(take,evtidx):
    """
    Python: Boolean  RPR_MIDI_DeleteEvt(MediaItem_Take take, Int evtidx)
    
    Delete a MIDI event.
    """
    a=_ft['MIDI_DeleteEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(evtidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_DeleteNote(take,noteidx):
    """
    Python: Boolean  RPR_MIDI_DeleteNote(MediaItem_Take take, Int noteidx)
    
    Delete a MIDI note.
    """
    a=_ft['MIDI_DeleteNote']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(noteidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_DeleteTextSysexEvt(take,textsyxevtidx):
    """
    Python: Boolean  RPR_MIDI_DeleteTextSysexEvt(MediaItem_Take take, Int textsyxevtidx)
    
    Delete a MIDI text or sysex event.
    """
    a=_ft['MIDI_DeleteTextSysexEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(textsyxevtidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_EnumSelCC(take,ccidx):
    """
    Python: Int  RPR_MIDI_EnumSelCC(MediaItem_Take take, Int ccidx)
    
    Returns the index of the next selected MIDI CC event after ccidx (-1 if there are no more selected events).
    """
    a=_ft['MIDI_EnumSelCC']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(ccidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_EnumSelEvts(take,evtidx):
    """
    Python: Int  RPR_MIDI_EnumSelEvts(MediaItem_Take take, Int evtidx)
    
    Returns the index of the next selected MIDI event after evtidx (-1 if there are no more selected events).
    """
    a=_ft['MIDI_EnumSelEvts']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(evtidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_EnumSelNotes(take,noteidx):
    """
    Python: Int  RPR_MIDI_EnumSelNotes(MediaItem_Take take, Int noteidx)
    
    Returns the index of the next selected MIDI note after noteidx (-1 if there are no more selected events).
    """
    a=_ft['MIDI_EnumSelNotes']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(noteidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_EnumSelTextSysexEvts(take,textsyxidx):
    """
    Python: Int  RPR_MIDI_EnumSelTextSysexEvts(MediaItem_Take take, Int textsyxidx)
    
    Returns the index of the next selected MIDI text/sysex event after textsyxidx (-1 if there are no more selected events).
    """
    a=_ft['MIDI_EnumSelTextSysexEvts']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(textsyxidx))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_GetAllEvts(take,bufNeedBig,bufNeedBig_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, String bufNeedBig, Int bufNeedBig_sz) = RPR_MIDI_GetAllEvts(take, bufNeedBig, bufNeedBig_sz)
    
    Get all MIDI data. MIDI buffer is returned as a list of { int offset, char flag, int msglen, unsigned char msg[] }. offset: MIDI ticks from previous event, flag: &1=selected &2=muted, msglen: byte length of msg (usually 3), msg: the MIDI message. For tick intervals longer than a 32 bit word can represent, zero-length meta events may be placed between valid events. See MIDI_SetAllEvts
    .
    """
    a=_ft['MIDI_GetAllEvts']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packs(bufNeedBig),c_int(bufNeedBig_sz))
    r=f(t[0],t[1],byref(t[2]))
    return (r,take,rpr_unpacks(t[1]),int(t[2].value))
     
def RPR_MIDI_GetCC(take,ccidx,selectedOut,mutedOut,ppqposOut,chanmsgOut,chanOut,msg2Out,msg3Out):
    """
    Python: (Boolean retval, MediaItem_Take take, Int ccidx, Boolean selectedOut, Boolean mutedOut, Float ppqposOut, Int chanmsgOut, Int chanOut, Int msg2Out, Int msg3Out) = RPR_MIDI_GetCC(take, ccidx, selectedOut, mutedOut, ppqposOut, chanmsgOut, chanOut, msg2Out, msg3Out)
    
    Get MIDI CC event properties.
    """
    a=_ft['MIDI_GetCC']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(ccidx),c_byte(selectedOut),c_byte(mutedOut),c_double(ppqposOut),c_int(chanmsgOut),c_int(chanOut),c_int(msg2Out),c_int(msg3Out))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]))
    return (r,take,ccidx,int(t[2].value),int(t[3].value),float(t[4].value),int(t[5].value),int(t[6].value),int(t[7].value),int(t[8].value))
     
def RPR_MIDI_GetEvt(take,evtidx,selectedOut,mutedOut,ppqposOut,msg,msg_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int evtidx, Boolean selectedOut, Boolean mutedOut, Float ppqposOut, String msg, Int msg_sz) = RPR_MIDI_GetEvt(take, evtidx, selectedOut, mutedOut, ppqposOut, msg, msg_sz)
    
    Get MIDI event properties.
    """
    a=_ft['MIDI_GetEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_char_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(evtidx),c_byte(selectedOut),c_byte(mutedOut),c_double(ppqposOut),rpr_packs(msg),c_int(msg_sz))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),t[5],byref(t[6]))
    return (r,take,evtidx,int(t[2].value),int(t[3].value),float(t[4].value),rpr_unpacks(t[5]),int(t[6].value))
     
def RPR_MIDI_GetGrid(take,swingOutOptional,noteLenOutOptional):
    """
    Python: (Float retval, MediaItem_Take take, Float swingOutOptional, Float noteLenOutOptional) = RPR_MIDI_GetGrid(take, swingOutOptional, noteLenOutOptional)
    
    Returns the most recent MIDI editor grid size for this MIDI take, in QN. Swing is between 0 and 1. Note length is 0 if it follows the grid size.
    """
    a=_ft['MIDI_GetGrid']
    f=CFUNCTYPE(c_double,c_uint64,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(swingOutOptional),c_double(noteLenOutOptional))
    r=f(t[0],byref(t[1]),byref(t[2]))
    return (r,take,float(t[1].value),float(t[2].value))
     
def RPR_MIDI_GetHash(take,notesonly,Hash,hash_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Boolean notesonly, String hash, Int hash_sz) = RPR_MIDI_GetHash(take, notesonly, hash, hash_sz)
    
    Get a string that only changes when the MIDI data changes. If notesonly==true, then the string changes only when the MIDI notes change. See MIDI_GetTrackHash
    """
    a=_ft['MIDI_GetHash']
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(notesonly),rpr_packs(Hash),c_int(hash_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,take,notesonly,rpr_unpacks(t[2]),hash_sz)
     
def RPR_MIDI_GetNote(take,noteidx,selectedOut,mutedOut,startppqposOut,endppqposOut,chanOut,pitchOut,velOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Int noteidx, Boolean selectedOut, Boolean mutedOut, Float startppqposOut, Float endppqposOut, Int chanOut, Int pitchOut, Int velOut) = RPR_MIDI_GetNote(take, noteidx, selectedOut, mutedOut, startppqposOut, endppqposOut, chanOut, pitchOut, velOut)
    
    Get MIDI note properties.
    """
    a=_ft['MIDI_GetNote']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(noteidx),c_byte(selectedOut),c_byte(mutedOut),c_double(startppqposOut),c_double(endppqposOut),c_int(chanOut),c_int(pitchOut),c_int(velOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]))
    return (r,take,noteidx,int(t[2].value),int(t[3].value),float(t[4].value),float(t[5].value),int(t[6].value),int(t[7].value),int(t[8].value))
     
def RPR_MIDI_GetPPQPos_EndOfMeasure(take,ppqpos):
    """
    Python: Float  RPR_MIDI_GetPPQPos_EndOfMeasure(MediaItem_Take take, Float ppqpos)
    
    Returns the MIDI tick (ppq) position corresponding to the end of the measure.
    """
    a=_ft['MIDI_GetPPQPos_EndOfMeasure']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(ppqpos))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_GetPPQPos_StartOfMeasure(take,ppqpos):
    """
    Python: Float  RPR_MIDI_GetPPQPos_StartOfMeasure(MediaItem_Take take, Float ppqpos)
    
    Returns the MIDI tick (ppq) position corresponding to the start of the measure.
    """
    a=_ft['MIDI_GetPPQPos_StartOfMeasure']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(ppqpos))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_GetPPQPosFromProjQN(take,projqn):
    """
    Python: Float  RPR_MIDI_GetPPQPosFromProjQN(MediaItem_Take take, Float projqn)
    
    Returns the MIDI tick (ppq) position corresponding to a specific project time in quarter notes.
    """
    a=_ft['MIDI_GetPPQPosFromProjQN']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(projqn))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_GetPPQPosFromProjTime(take,projtime):
    """
    Python: Float  RPR_MIDI_GetPPQPosFromProjTime(MediaItem_Take take, Float projtime)
    
    Returns the MIDI tick (ppq) position corresponding to a specific project time in seconds.
    """
    a=_ft['MIDI_GetPPQPosFromProjTime']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(projtime))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_GetProjQNFromPPQPos(take,ppqpos):
    """
    Python: Float  RPR_MIDI_GetProjQNFromPPQPos(MediaItem_Take take, Float ppqpos)
    
    Returns the project time in quarter notes corresponding to a specific MIDI tick (ppq) position.
    """
    a=_ft['MIDI_GetProjQNFromPPQPos']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(ppqpos))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_GetProjTimeFromPPQPos(take,ppqpos):
    """
    Python: Float  RPR_MIDI_GetProjTimeFromPPQPos(MediaItem_Take take, Float ppqpos)
    
    Returns the project time in seconds corresponding to a specific MIDI tick (ppq) position.
    """
    a=_ft['MIDI_GetProjTimeFromPPQPos']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_double(ppqpos))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDI_GetScale(take,rootOut,scaleOut,name,name_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int rootOut, Int scaleOut, String name, Int name_sz) = RPR_MIDI_GetScale(take, rootOut, scaleOut, name, name_sz)
    
    Get the active scale in the media source, if any. root 0=C, 1=C#, etc. scale &0x1=root, &0x2=minor 2nd, &0x4=major 2nd, &0x8=minor 3rd, &0xF=fourth, etc.
    """
    a=_ft['MIDI_GetScale']
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p,c_void_p,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(rootOut),c_int(scaleOut),rpr_packs(name),c_int(name_sz))
    r=f(t[0],byref(t[1]),byref(t[2]),t[3],t[4])
    return (r,take,int(t[1].value),int(t[2].value),rpr_unpacks(t[3]),name_sz)
     
def RPR_MIDI_GetTextSysexEvt(take,textsyxevtidx,selectedOutOptional,mutedOutOptional,ppqposOutOptional,typeOutOptional,msgOptional,msgOptional_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int textsyxevtidx, Boolean selectedOutOptional, Boolean mutedOutOptional, Float ppqposOutOptional, Int typeOutOptional, String msgOptional, Int msgOptional_sz) = RPR_MIDI_GetTextSysexEvt(take, textsyxevtidx, selectedOutOptional, mutedOutOptional, ppqposOutOptional, typeOutOptional, msgOptional, msgOptional_sz)
    
    Get MIDI meta-event properties. Allowable types are -1:sysex (msg should not include bounding F0..F7), 1-7:MIDI text event types.
    """
    a=_ft['MIDI_GetTextSysexEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_char_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(textsyxevtidx),c_byte(selectedOutOptional),c_byte(mutedOutOptional),c_double(ppqposOutOptional),c_int(typeOutOptional),rpr_packs(msgOptional),c_int(msgOptional_sz))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),t[6],byref(t[7]))
    return (r,take,textsyxevtidx,int(t[2].value),int(t[3].value),float(t[4].value),int(t[5].value),rpr_unpacks(t[6]),int(t[7].value))
     
def RPR_MIDI_GetTrackHash(track,notesonly,Hash,hash_sz):
    """
    Python: (Boolean retval, MediaTrack track, Boolean notesonly, String hash, Int hash_sz) = RPR_MIDI_GetTrackHash(track, notesonly, hash, hash_sz)
    
    Get a string that only changes when the MIDI data changes. If notesonly==true, then the string changes only when the MIDI notes change. See MIDI_GetHash
    """
    a=_ft['MIDI_GetTrackHash']
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_byte(notesonly),rpr_packs(Hash),c_int(hash_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,notesonly,rpr_unpacks(t[2]),hash_sz)
     
def RPR_MIDI_InsertCC(take,selected,muted,ppqpos,chanmsg,chan,msg2,msg3):
    """
    Python: Boolean  RPR_MIDI_InsertCC(MediaItem_Take take, Boolean selected, Boolean muted, Float ppqpos, Int chanmsg, Int chan, Int msg2, Int msg3)
    
    Insert a new MIDI CC event.
    """
    a=_ft['MIDI_InsertCC']
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_byte,c_double,c_int,c_int,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(selected),c_byte(muted),c_double(ppqpos),c_int(chanmsg),c_int(chan),c_int(msg2),c_int(msg3))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7])
    return r
     
def RPR_MIDI_InsertEvt(take,selected,muted,ppqpos,bytestr,bytestr_sz):
    """
    Python: Boolean  RPR_MIDI_InsertEvt(MediaItem_Take take, Boolean selected, Boolean muted, Float ppqpos, String bytestr, Int bytestr_sz)
    
    Insert a new MIDI event.
    """
    a=_ft['MIDI_InsertEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_byte,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(selected),c_byte(muted),c_double(ppqpos),rpr_packsc(bytestr),c_int(bytestr_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def RPR_MIDI_InsertNote(take,selected,muted,startppqpos,endppqpos,chan,pitch,vel,noSortInOptional):
    """
    Python: Boolean  RPR_MIDI_InsertNote(MediaItem_Take take, Boolean selected, Boolean muted, Float startppqpos, Float endppqpos, Int chan, Int pitch, Int vel, const bool noSortInOptional)
    
    Insert a new MIDI note. Set noSort if inserting multiple events, then call MIDI_Sort when done.
    """
    a=_ft['MIDI_InsertNote']
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_byte,c_double,c_double,c_int,c_int,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(selected),c_byte(muted),c_double(startppqpos),c_double(endppqpos),c_int(chan),c_int(pitch),c_int(vel),c_byte(noSortInOptional))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],byref(t[8]))
    return (r,take,selected,muted,startppqpos,endppqpos,chan,pitch,vel,int(t[8].value))
     
def RPR_MIDI_InsertTextSysexEvt(take,selected,muted,ppqpos,Type,bytestr,bytestr_sz):
    """
    Python: Boolean  RPR_MIDI_InsertTextSysexEvt(MediaItem_Take take, Boolean selected, Boolean muted, Float ppqpos, Int type, String bytestr, Int bytestr_sz)
    
    Insert a new MIDI text or sysex event. Allowable types are -1:sysex (msg should not include bounding F0..F7), 1-7:MIDI text event types.
    """
    a=_ft['MIDI_InsertTextSysexEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_byte,c_byte,c_double,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(selected),c_byte(muted),c_double(ppqpos),c_int(Type),rpr_packsc(bytestr),c_int(bytestr_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return r
     
def RPR_midi_reinit():
    """
    Python: RPR_midi_reinit()
    
    Reset all MIDI devices
    """
    a=_ft['midi_reinit']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_MIDI_SelectAll(take,select):
    """
    Python: RPR_MIDI_SelectAll(MediaItem_Take take, Boolean select)
    
    Select or deselect all MIDI content.
    """
    a=_ft['MIDI_SelectAll']
    f=CFUNCTYPE(None,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_byte(select))
    f(t[0],t[1])
     
def RPR_MIDI_SetAllEvts(take,buf,buf_sz):
    """
    Python: Boolean  RPR_MIDI_SetAllEvts(MediaItem_Take take, String buf, Int buf_sz)
    
    Set all MIDI data. MIDI buffer is passed in as a list of { int offset, char flag, int msglen, unsigned char msg[] }. offset: MIDI ticks from previous event, flag: &1=selected &2=muted, msglen: byte length of msg (usually 3), msg: the MIDI message. For tick intervals longer than a 32 bit word can represent, zero-length meta events may be placed between valid events. See MIDI_GetAllEvts
    .
    """
    a=_ft['MIDI_SetAllEvts']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packsc(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_MIDI_SetCC(take,ccidx,selectedInOptional,mutedInOptional,ppqposInOptional,chanmsgInOptional,chanInOptional,msg2InOptional,msg3InOptional,noSortInOptional):
    """
    Python: Boolean  RPR_MIDI_SetCC(MediaItem_Take take, Int ccidx, const bool selectedInOptional, const bool mutedInOptional, const double ppqposInOptional, const int chanmsgInOptional, const int chanInOptional, const int msg2InOptional, const int msg3InOptional, const bool noSortInOptional)
    
    Set MIDI CC event properties. Properties passed as NULL will not be set. set noSort if setting multiple events, then call MIDI_Sort when done.
    """
    a=_ft['MIDI_SetCC']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(ccidx),c_byte(selectedInOptional),c_byte(mutedInOptional),c_double(ppqposInOptional),c_int(chanmsgInOptional),c_int(chanInOptional),c_int(msg2InOptional),c_int(msg3InOptional),c_byte(noSortInOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]),byref(t[9]))
    return (r,take,ccidx,int(t[2].value),int(t[3].value),float(t[4].value),int(t[5].value),int(t[6].value),int(t[7].value),int(t[8].value),int(t[9].value))
     
def RPR_MIDI_SetEvt(take,evtidx,selectedInOptional,mutedInOptional,ppqposInOptional,msgOptional,msgOptional_sz,noSortInOptional):
    """
    Python: Boolean  RPR_MIDI_SetEvt(MediaItem_Take take, Int evtidx, const bool selectedInOptional, const bool mutedInOptional, const double ppqposInOptional, String msgOptional, Int msgOptional_sz, const bool noSortInOptional)
    
    Set MIDI event properties. Properties passed as NULL will not be set.  set noSort if setting multiple events, then call MIDI_Sort when done.
    """
    a=_ft['MIDI_SetEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_char_p,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(evtidx),c_byte(selectedInOptional),c_byte(mutedInOptional),c_double(ppqposInOptional),rpr_packsc(msgOptional),c_int(msgOptional_sz),c_byte(noSortInOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),t[5],t[6],byref(t[7]))
    return (r,take,evtidx,int(t[2].value),int(t[3].value),float(t[4].value),msgOptional,msgOptional_sz,int(t[7].value))
     
def RPR_MIDI_SetItemExtents(item,startQN,endQN):
    """
    Python: Boolean  RPR_MIDI_SetItemExtents(MediaItem item, Float startQN, Float endQN)
    
    Set the start/end positions of a media item that contains a MIDI take.
    """
    a=_ft['MIDI_SetItemExtents']
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_double)(a)
    t=(rpr_packp('MediaItem*',item),c_double(startQN),c_double(endQN))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_MIDI_SetNote(take,noteidx,selectedInOptional,mutedInOptional,startppqposInOptional,endppqposInOptional,chanInOptional,pitchInOptional,velInOptional,noSortInOptional):
    """
    Python: Boolean  RPR_MIDI_SetNote(MediaItem_Take take, Int noteidx, const bool selectedInOptional, const bool mutedInOptional, const double startppqposInOptional, const double endppqposInOptional, const int chanInOptional, const int pitchInOptional, const int velInOptional, const bool noSortInOptional)
    
    Set MIDI note properties. Properties passed as NULL (or negative values) will not be set. Set noSort if setting multiple events, then call MIDI_Sort when done. Setting multiple note start positions at once is done more safely by deleting and re-inserting the notes.
    """
    a=_ft['MIDI_SetNote']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(noteidx),c_byte(selectedInOptional),c_byte(mutedInOptional),c_double(startppqposInOptional),c_double(endppqposInOptional),c_int(chanInOptional),c_int(pitchInOptional),c_int(velInOptional),c_byte(noSortInOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]),byref(t[9]))
    return (r,take,noteidx,int(t[2].value),int(t[3].value),float(t[4].value),float(t[5].value),int(t[6].value),int(t[7].value),int(t[8].value),int(t[9].value))
     
def RPR_MIDI_SetTextSysexEvt(take,textsyxevtidx,selectedInOptional,mutedInOptional,ppqposInOptional,typeInOptional,msgOptional,msgOptional_sz,noSortInOptional):
    """
    Python: Boolean  RPR_MIDI_SetTextSysexEvt(MediaItem_Take take, Int textsyxevtidx, const bool selectedInOptional, const bool mutedInOptional, const double ppqposInOptional, const int typeInOptional, String msgOptional, Int msgOptional_sz, const bool noSortInOptional)
    
    Set MIDI text or sysex event properties. Properties passed as NULL will not be set. Allowable types are -1:sysex (msg should not include bounding F0..F7), 1-7:MIDI text event types. set noSort if setting multiple events, then call MIDI_Sort when done.
    """
    a=_ft['MIDI_SetTextSysexEvt']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_char_p,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(textsyxevtidx),c_byte(selectedInOptional),c_byte(mutedInOptional),c_double(ppqposInOptional),c_int(typeInOptional),rpr_packsc(msgOptional),c_int(msgOptional_sz),c_byte(noSortInOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),t[6],t[7],byref(t[8]))
    return (r,take,textsyxevtidx,int(t[2].value),int(t[3].value),float(t[4].value),int(t[5].value),msgOptional,msgOptional_sz,int(t[8].value))
     
def RPR_MIDI_Sort(take):
    """
    Python: RPR_MIDI_Sort(MediaItem_Take take)
    
    Sort MIDI events after multiple calls to MIDI_SetNote, MIDI_SetCC, etc.
    """
    a=_ft['MIDI_Sort']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    f(t[0])
     
def RPR_MIDIEditor_GetActive():
    """
    Python: HWND  RPR_MIDIEditor_GetActive()
    
    get a pointer to the focused MIDI editor window
    
    see MIDIEditor_GetMode
    , MIDIEditor_OnCommand
    """
    a=_ft['MIDIEditor_GetActive']
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('HWND',r)
     
def RPR_MIDIEditor_GetMode(midieditor):
    """
    Python: Int  RPR_MIDIEditor_GetMode(HWND midieditor)
    
    get the mode of a MIDI editor (0=piano roll, 1=event list, -1=invalid editor)
    
    see MIDIEditor_GetActive
    , MIDIEditor_OnCommand
    """
    a=_ft['MIDIEditor_GetMode']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('HWND',midieditor),)
    r=f(t[0])
    return r
     
def RPR_MIDIEditor_GetSetting_int(midieditor,setting_desc):
    """
    Python: Int  RPR_MIDIEditor_GetSetting_int(HWND midieditor, String setting_desc)
    
    Get settings from a MIDI editor. setting_desc can be:
    
    snap_enabled: returns 0 or 1
    
    active_note_row: returns 0-127
    
    last_clicked_cc_lane: returns 0-127=CC, 0x100|(0-31)=14-bit CC, 0x200=velocity, 0x201=pitch, 0x202=program, 0x203=channel pressure, 0x204=bank/program select, 0x205=text, 0x206=sysex, 0x207=off velocity
    
    default_note_vel: returns 0-127
    
    default_note_chan: returns 0-15
    
    default_note_len: returns default length in MIDI ticks
    
    scale_enabled: returns 0-1
    
    scale_root: returns 0-12 (0=C)
    
    if setting_desc is unsupported, the function returns -1.
    
    See MIDIEditor_GetActive
    , MIDIEditor_GetSetting_str
    """
    a=_ft['MIDIEditor_GetSetting_int']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p)(a)
    t=(rpr_packp('HWND',midieditor),rpr_packsc(setting_desc))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDIEditor_GetSetting_str(midieditor,setting_desc,buf,buf_sz):
    """
    Python: (Boolean retval, HWND midieditor, String setting_desc, String buf, Int buf_sz) = RPR_MIDIEditor_GetSetting_str(midieditor, setting_desc, buf, buf_sz)
    
    Get settings from a MIDI editor. setting_desc can be:
    
    last_clicked_cc_lane: returns text description ("velocity", "pitch", etc)
    
    scale: returns the scale record, for example "102034050607" for a major scale
    
    if setting_desc is unsupported, the function returns false.
    
    See MIDIEditor_GetActive
    , MIDIEditor_GetSetting_int
    """
    a=_ft['MIDIEditor_GetSetting_str']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packp('HWND',midieditor),rpr_packsc(setting_desc),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,midieditor,setting_desc,rpr_unpacks(t[2]),buf_sz)
     
def RPR_MIDIEditor_GetTake(midieditor):
    """
    Python: MediaItem_Take  RPR_MIDIEditor_GetTake(HWND midieditor)
    
    get the take that is currently being edited in this MIDI editor
    """
    a=_ft['MIDIEditor_GetTake']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('HWND',midieditor),)
    r=f(t[0])
    return rpr_unpackp('MediaItem_Take*',r)
     
def RPR_MIDIEditor_LastFocused_OnCommand(command_id,islistviewcommand):
    """
    Python: Boolean  RPR_MIDIEditor_LastFocused_OnCommand(Int command_id, Boolean islistviewcommand)
    
    Send an action command to the last focused MIDI editor. Returns false if there is no MIDI editor open, or if the view mode (piano roll or event list) does not match the input.
    
    see MIDIEditor_OnCommand
    """
    a=_ft['MIDIEditor_LastFocused_OnCommand']
    f=CFUNCTYPE(c_byte,c_int,c_byte)(a)
    t=(c_int(command_id),c_byte(islistviewcommand))
    r=f(t[0],t[1])
    return r
     
def RPR_MIDIEditor_OnCommand(midieditor,command_id):
    """
    Python: Boolean  RPR_MIDIEditor_OnCommand(HWND midieditor, Int command_id)
    
    Send an action command to a MIDI editor. Returns false if the supplied MIDI editor pointer is not valid (not an open MIDI editor).
    
    see MIDIEditor_GetActive
    , MIDIEditor_LastFocused_OnCommand
    """
    a=_ft['MIDIEditor_OnCommand']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('HWND',midieditor),c_int(command_id))
    r=f(t[0],t[1])
    return r
     
def RPR_mkpanstr(strNeed64,pan):
    """
    Python: (String strNeed64, Float pan) = RPR_mkpanstr(strNeed64, pan)
    """
    a=_ft['mkpanstr']
    f=CFUNCTYPE(None,c_char_p,c_double)(a)
    t=(rpr_packs(strNeed64),c_double(pan))
    f(t[0],t[1])
    return (rpr_unpacks(t[0]),pan)
     
def RPR_mkvolpanstr(strNeed64,vol,pan):
    """
    Python: (String strNeed64, Float vol, Float pan) = RPR_mkvolpanstr(strNeed64, vol, pan)
    """
    a=_ft['mkvolpanstr']
    f=CFUNCTYPE(None,c_char_p,c_double,c_double)(a)
    t=(rpr_packs(strNeed64),c_double(vol),c_double(pan))
    f(t[0],t[1],t[2])
    return (rpr_unpacks(t[0]),vol,pan)
     
def RPR_mkvolstr(strNeed64,vol):
    """
    Python: (String strNeed64, Float vol) = RPR_mkvolstr(strNeed64, vol)
    """
    a=_ft['mkvolstr']
    f=CFUNCTYPE(None,c_char_p,c_double)(a)
    t=(rpr_packs(strNeed64),c_double(vol))
    f(t[0],t[1])
    return (rpr_unpacks(t[0]),vol)
     
def RPR_MoveEditCursor(adjamt,dosel):
    """
    Python: RPR_MoveEditCursor(Float adjamt, Boolean dosel)
    """
    a=_ft['MoveEditCursor']
    f=CFUNCTYPE(None,c_double,c_byte)(a)
    t=(c_double(adjamt),c_byte(dosel))
    f(t[0],t[1])
     
def RPR_MoveMediaItemToTrack(item,desttr):
    """
    Python: Boolean  RPR_MoveMediaItemToTrack(MediaItem item, MediaTrack desttr)
    
    returns TRUE if move succeeded
    """
    a=_ft['MoveMediaItemToTrack']
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packp('MediaTrack*',desttr))
    r=f(t[0],t[1])
    return r
     
def RPR_MuteAllTracks(mute):
    """
    Python: RPR_MuteAllTracks(Boolean mute)
    """
    a=_ft['MuteAllTracks']
    f=CFUNCTYPE(None,c_byte)(a)
    t=(c_byte(mute),)
    f(t[0])
     
def RPR_my_getViewport(r,sr,wantWorkArea):
    """
    Python: RPR_my_getViewport(RECT r, const RECT sr, Boolean wantWorkArea)
    """
    a=_ft['my_getViewport']
    f=CFUNCTYPE(None,c_uint64,c_uint64,c_byte)(a)
    t=(rpr_packp('RECT*',r),rpr_packp('RECT*',sr),c_byte(wantWorkArea))
    f(t[0],t[1],t[2])
     
def RPR_NamedCommandLookup(command_name):
    """
    Python: Int  RPR_NamedCommandLookup(String command_name)
    
    Get the command ID number for named command that was registered by an extension such as "_SWS_ABOUT" or "_113088d11ae641c193a2b7ede3041ad5" for a ReaScript or a custom action.
    """
    a=_ft['NamedCommandLookup']
    f=CFUNCTYPE(c_int,c_char_p)(a)
    t=(rpr_packsc(command_name),)
    r=f(t[0])
    return r
     
def RPR_OnPauseButton():
    """
    Python: RPR_OnPauseButton()
    
    direct way to simulate pause button hit
    """
    a=_ft['OnPauseButton']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_OnPauseButtonEx(proj):
    """
    Python: RPR_OnPauseButtonEx(ReaProject proj)
    
    direct way to simulate pause button hit
    """
    a=_ft['OnPauseButtonEx']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    f(t[0])
     
def RPR_OnPlayButton():
    """
    Python: RPR_OnPlayButton()
    
    direct way to simulate play button hit
    """
    a=_ft['OnPlayButton']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_OnPlayButtonEx(proj):
    """
    Python: RPR_OnPlayButtonEx(ReaProject proj)
    
    direct way to simulate play button hit
    """
    a=_ft['OnPlayButtonEx']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    f(t[0])
     
def RPR_OnStopButton():
    """
    Python: RPR_OnStopButton()
    
    direct way to simulate stop button hit
    """
    a=_ft['OnStopButton']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_OnStopButtonEx(proj):
    """
    Python: RPR_OnStopButtonEx(ReaProject proj)
    
    direct way to simulate stop button hit
    """
    a=_ft['OnStopButtonEx']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    f(t[0])
     
def RPR_OpenColorThemeFile(fn):
    """
    Python: Boolean  RPR_OpenColorThemeFile(String fn)
    """
    a=_ft['OpenColorThemeFile']
    f=CFUNCTYPE(c_byte,c_char_p)(a)
    t=(rpr_packsc(fn),)
    r=f(t[0])
    return r
     
def RPR_OpenMediaExplorer(mediafn,play):
    """
    Python: HWND  RPR_OpenMediaExplorer(String mediafn, Boolean play)
    
    Opens mediafn in the Media Explorer, play=true will play the file immediately (or toggle playback if mediafn was already open), =false will just select it.
    """
    a=_ft['OpenMediaExplorer']
    f=CFUNCTYPE(c_uint64,c_char_p,c_byte)(a)
    t=(rpr_packsc(mediafn),c_byte(play))
    r=f(t[0],t[1])
    return rpr_unpackp('HWND',r)
     
def RPR_OscLocalMessageToHost(message,valueInOptional):
    """
    Python: RPR_OscLocalMessageToHost(String message, const double valueInOptional)
    
    Send an OSC message directly to REAPER. The value argument may be NULL. The message will be matched against the default OSC patterns. Only supported if control surface support was enabled when installing REAPER.
    """
    a=_ft['OscLocalMessageToHost']
    f=CFUNCTYPE(None,c_char_p,c_void_p)(a)
    t=(rpr_packsc(message),c_double(valueInOptional))
    f(t[0],byref(t[1]))
    return (message,float(t[1].value))
     
def RPR_parse_timestr(buf):
    """
    Python: Float  RPR_parse_timestr(String buf)
    
    Parse hh:mm:ss.sss time string, return time in seconds (or 0.0 on error). See parse_timestr_pos
    , parse_timestr_len
    .
    """
    a=_ft['parse_timestr']
    f=CFUNCTYPE(c_double,c_char_p)(a)
    t=(rpr_packsc(buf),)
    r=f(t[0])
    return r
     
def RPR_parse_timestr_len(buf,offset,modeoverride):
    """
    Python: Float  RPR_parse_timestr_len(String buf, Float offset, Int modeoverride)
    
    time formatting mode overrides: -1=proj default.
    
    0=time
    
    1=measures.beats + time
    
    2=measures.beats
    
    3=seconds
    
    4=samples
    
    5=h:m:s:f
    """
    a=_ft['parse_timestr_len']
    f=CFUNCTYPE(c_double,c_char_p,c_double,c_int)(a)
    t=(rpr_packsc(buf),c_double(offset),c_int(modeoverride))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_parse_timestr_pos(buf,modeoverride):
    """
    Python: Float  RPR_parse_timestr_pos(String buf, Int modeoverride)
    
    Parse time string, time formatting mode overrides: -1=proj default.
    
    0=time
    
    1=measures.beats + time
    
    2=measures.beats
    
    3=seconds
    
    4=samples
    
    5=h:m:s:f
    """
    a=_ft['parse_timestr_pos']
    f=CFUNCTYPE(c_double,c_char_p,c_int)(a)
    t=(rpr_packsc(buf),c_int(modeoverride))
    r=f(t[0],t[1])
    return r
     
def RPR_parsepanstr(Str):
    """
    Python: Float  RPR_parsepanstr(String str)
    """
    a=_ft['parsepanstr']
    f=CFUNCTYPE(c_double,c_char_p)(a)
    t=(rpr_packsc(Str),)
    r=f(t[0])
    return r
     
def RPR_PCM_Sink_Enum(idx,descstrOut):
    """
    Python: Unknown  RPR_PCM_Sink_Enum(Int idx, String descstrOut)
    """
    a=_ft['PCM_Sink_Enum']
    f=CFUNCTYPE(c_int,c_int,c_uint64)(a)
    t=(c_int(idx),rpr_packp('char**',descstrOut))
    r=f(t[0],t[1])
    return r
     
def RPR_PCM_Sink_GetExtension(data,data_sz):
    """
    Python: String  RPR_PCM_Sink_GetExtension(String data, Int data_sz)
    """
    a=_ft['PCM_Sink_GetExtension']
    f=CFUNCTYPE(c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(data),c_int(data_sz))
    r=f(t[0],t[1])
    return str(r.decode())
     
def RPR_PCM_Sink_ShowConfig(cfg,cfg_sz,hwndParent):
    """
    Python: HWND  RPR_PCM_Sink_ShowConfig(String cfg, Int cfg_sz, HWND hwndParent)
    """
    a=_ft['PCM_Sink_ShowConfig']
    f=CFUNCTYPE(c_uint64,c_char_p,c_int,c_uint64)(a)
    t=(rpr_packsc(cfg),c_int(cfg_sz),rpr_packp('HWND',hwndParent))
    r=f(t[0],t[1],t[2])
    return rpr_unpackp('HWND',r)
     
def RPR_PCM_Source_CreateFromFile(filename):
    """
    Python: PCM_source  RPR_PCM_Source_CreateFromFile(String filename)
    
    See PCM_Source_CreateFromFileEx
    .
    """
    a=_ft['PCM_Source_CreateFromFile']
    f=CFUNCTYPE(c_uint64,c_char_p)(a)
    t=(rpr_packsc(filename),)
    r=f(t[0])
    return rpr_unpackp('PCM_source*',r)
     
def RPR_PCM_Source_CreateFromFileEx(filename,forcenoMidiImp):
    """
    Python: PCM_source  RPR_PCM_Source_CreateFromFileEx(String filename, Boolean forcenoMidiImp)
    
    Create a PCM_source from filename, and override pref of MIDI files being imported as in-project MIDI events.
    """
    a=_ft['PCM_Source_CreateFromFileEx']
    f=CFUNCTYPE(c_uint64,c_char_p,c_byte)(a)
    t=(rpr_packsc(filename),c_byte(forcenoMidiImp))
    r=f(t[0],t[1])
    return rpr_unpackp('PCM_source*',r)
     
def RPR_PCM_Source_CreateFromType(sourcetype):
    """
    Python: PCM_source  RPR_PCM_Source_CreateFromType(String sourcetype)
    
    Create a PCM_source from a "type" (use this if you're going to load its state via LoadState/ProjectStateContext).
    
    Valid types include "WAVE", "MIDI", or whatever plug-ins define as well.
    """
    a=_ft['PCM_Source_CreateFromType']
    f=CFUNCTYPE(c_uint64,c_char_p)(a)
    t=(rpr_packsc(sourcetype),)
    r=f(t[0])
    return rpr_unpackp('PCM_source*',r)
     
def RPR_PCM_Source_Destroy(src):
    """
    Python: RPR_PCM_Source_Destroy(PCM_source src)
    
    Deletes a PCM_source -- be sure that you remove any project reference before deleting a source
    """
    a=_ft['PCM_Source_Destroy']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('PCM_source*',src),)
    f(t[0])
     
def RPR_PCM_Source_GetPeaks(src,peakrate,starttime,numchannels,numsamplesperchannel,want_extra_type,buf):
    """
    Python: (Int retval, PCM_source src, Float peakrate, Float starttime, Int numchannels, Int numsamplesperchannel, Int want_extra_type, Float buf) = RPR_PCM_Source_GetPeaks(src, peakrate, starttime, numchannels, numsamplesperchannel, want_extra_type, buf)
    
    Gets block of peak samples to buf. Note that the peak samples are interleaved, but in two or three blocks (maximums, then minimums, then extra). Return value has 20 bits of returned sample count, then 4 bits of output_mode (0xf00000), then a bit to signify whether extra_type was available (0x1000000). extra_type can be 115 ('s') for spectral information, which will return peak samples as integers with the low 15 bits frequency, next 14 bits tonality.
    """
    a=_ft['PCM_Source_GetPeaks']
    f=CFUNCTYPE(c_int,c_uint64,c_double,c_double,c_int,c_int,c_int,c_void_p)(a)
    t=(rpr_packp('PCM_source*',src),c_double(peakrate),c_double(starttime),c_int(numchannels),c_int(numsamplesperchannel),c_int(want_extra_type),c_double(buf))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],byref(t[6]))
    return (r,src,peakrate,starttime,numchannels,numsamplesperchannel,want_extra_type,float(t[6].value))
     
def RPR_PCM_Source_GetSectionInfo(src,offsOut,lenOut,revOut):
    """
    Python: (Boolean retval, PCM_source src, Float offsOut, Float lenOut, Boolean revOut) = RPR_PCM_Source_GetSectionInfo(src, offsOut, lenOut, revOut)
    
    If a section/reverse block, retrieves offset/len/reverse. return true if success
    """
    a=_ft['PCM_Source_GetSectionInfo']
    f=CFUNCTYPE(c_byte,c_uint64,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('PCM_source*',src),c_double(offsOut),c_double(lenOut),c_byte(revOut))
    r=f(t[0],byref(t[1]),byref(t[2]),byref(t[3]))
    return (r,src,float(t[1].value),float(t[2].value),int(t[3].value))
     
def RPR_PluginWantsAlwaysRunFx(amt):
    """
    Python: RPR_PluginWantsAlwaysRunFx(Int amt)
    """
    a=_ft['PluginWantsAlwaysRunFx']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(amt),)
    f(t[0])
     
def RPR_PreventUIRefresh(prevent_count):
    """
    Python: RPR_PreventUIRefresh(Int prevent_count)
    
    adds prevent_count to the UI refresh prevention state; always add then remove the same amount, or major disfunction will occur
    """
    a=_ft['PreventUIRefresh']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(prevent_count),)
    f(t[0])
     
def RPR_ReaScriptError(errmsg):
    """
    Python: RPR_ReaScriptError(String errmsg)
    
    Causes REAPER to display the error message after the current ReaScript finishes.
    """
    a=_ft['ReaScriptError']
    f=CFUNCTYPE(None,c_char_p)(a)
    t=(rpr_packsc(errmsg),)
    f(t[0])
     
def RPR_RecursiveCreateDirectory(path,ignored):
    """
    Python: Int  RPR_RecursiveCreateDirectory(String path, Unknown ignored)
    
    returns positive value on success, 0 on failure.
    """
    a=_ft['RecursiveCreateDirectory']
    f=CFUNCTYPE(c_int,c_char_p,c_int)(a)
    t=(rpr_packsc(path),c_int(ignored))
    r=f(t[0],t[1])
    return r
     
def RPR_RefreshToolbar(command_id):
    """
    Python: RPR_RefreshToolbar(Int command_id)
    
    See RefreshToolbar2
    .
    """
    a=_ft['RefreshToolbar']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(command_id),)
    f(t[0])
     
def RPR_RefreshToolbar2(section_id,command_id):
    """
    Python: RPR_RefreshToolbar2(Int section_id, Int command_id)
    
    Refresh the toolbar button states of a toggle action.
    """
    a=_ft['RefreshToolbar2']
    f=CFUNCTYPE(None,c_int,c_int)(a)
    t=(c_int(section_id),c_int(command_id))
    f(t[0],t[1])
     
def RPR_relative_fn(In,out,out_sz):
    """
    Python: (String in, String out, Int out_sz) = RPR_relative_fn(in, out, out_sz)
    
    Makes a filename "in" relative to the current project, if any.
    """
    a=_ft['relative_fn']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(In),rpr_packs(out),c_int(out_sz))
    f(t[0],t[1],t[2])
    return (In,rpr_unpacks(t[1]),out_sz)
     
def RPR_RemoveTrackSend(tr,category,sendidx):
    """
    Python: Boolean  RPR_RemoveTrackSend(MediaTrack tr, Int category, Int sendidx)
    
    Remove a send/receive/hardware output, return true on success. category is <0 for receives, 0=sends, >0 for hardware outputs. See CreateTrackSend
    , GetSetTrackSendInfo
    , GetTrackSendInfo_Value
    , SetTrackSendInfo_Value
    , GetTrackNumSends
    .
    """
    a=_ft['RemoveTrackSend']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(category),c_int(sendidx))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_RenderFileSection(source_filename,target_filename,start_percent,end_percent,playrate):
    """
    Python: Boolean  RPR_RenderFileSection(String source_filename, String target_filename, Float start_percent, Float end_percent, Float playrate)
    
    Not available while playing back.
    """
    a=_ft['RenderFileSection']
    f=CFUNCTYPE(c_byte,c_char_p,c_char_p,c_double,c_double,c_double)(a)
    t=(rpr_packsc(source_filename),rpr_packsc(target_filename),c_double(start_percent),c_double(end_percent),c_double(playrate))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def RPR_ReorderSelectedTracks(beforeTrackIdx,makePrevFolder):
    """
    Python: Boolean  RPR_ReorderSelectedTracks(Int beforeTrackIdx, Int makePrevFolder)
    
    Moves all selected tracks to immediately above track specified by index beforeTrackIdx, returns false if no tracks were selected. makePrevFolder=0 for normal, 1 = as child of track preceding track specified by beforeTrackIdx, 2 = if track preceding track specified by beforeTrackIdx is last track in folder, extend folder
    """
    a=_ft['ReorderSelectedTracks']
    f=CFUNCTYPE(c_byte,c_int,c_int)(a)
    t=(c_int(beforeTrackIdx),c_int(makePrevFolder))
    r=f(t[0],t[1])
    return r
     
def RPR_Resample_EnumModes(mode):
    """
    Python: String  RPR_Resample_EnumModes(Int mode)
    """
    a=_ft['Resample_EnumModes']
    f=CFUNCTYPE(c_char_p,c_int)(a)
    t=(c_int(mode),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_resolve_fn(In,out,out_sz):
    """
    Python: (String in, String out, Int out_sz) = RPR_resolve_fn(in, out, out_sz)
    
    See resolve_fn2
    .
    """
    a=_ft['resolve_fn']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(In),rpr_packs(out),c_int(out_sz))
    f(t[0],t[1],t[2])
    return (In,rpr_unpacks(t[1]),out_sz)
     
def RPR_resolve_fn2(In,out,out_sz,checkSubDirOptional):
    """
    Python: (String in, String out, Int out_sz, String checkSubDirOptional) = RPR_resolve_fn2(in, out, out_sz, checkSubDirOptional)
    
    Resolves a filename "in" by using project settings etc. If no file found, out will be a copy of in.
    """
    a=_ft['resolve_fn2']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_int,c_char_p)(a)
    t=(rpr_packsc(In),rpr_packs(out),c_int(out_sz),rpr_packsc(checkSubDirOptional))
    f(t[0],t[1],t[2],t[3])
    return (In,rpr_unpacks(t[1]),out_sz,checkSubDirOptional)
     
def RPR_ReverseNamedCommandLookup(command_id):
    """
    Python: String  RPR_ReverseNamedCommandLookup(Int command_id)
    
    Get the named command for the given command ID. The returned string will not start with '_' (e.g. it will return "SWS_ABOUT"), it will be NULL if command_id is a native action.
    """
    a=_ft['ReverseNamedCommandLookup']
    f=CFUNCTYPE(c_char_p,c_int)(a)
    t=(c_int(command_id),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_ScaleFromEnvelopeMode(scaling_mode,val):
    """
    Python: Float  RPR_ScaleFromEnvelopeMode(Int scaling_mode, Float val)
    
    See GetEnvelopeScalingMode
    .
    """
    a=_ft['ScaleFromEnvelopeMode']
    f=CFUNCTYPE(c_double,c_int,c_double)(a)
    t=(c_int(scaling_mode),c_double(val))
    r=f(t[0],t[1])
    return r
     
def RPR_ScaleToEnvelopeMode(scaling_mode,val):
    """
    Python: Float  RPR_ScaleToEnvelopeMode(Int scaling_mode, Float val)
    
    See GetEnvelopeScalingMode
    .
    """
    a=_ft['ScaleToEnvelopeMode']
    f=CFUNCTYPE(c_double,c_int,c_double)(a)
    t=(c_int(scaling_mode),c_double(val))
    r=f(t[0],t[1])
    return r
     
def RPR_SelectAllMediaItems(proj,selected):
    """
    Python: RPR_SelectAllMediaItems(ReaProject proj, Boolean selected)
    """
    a=_ft['SelectAllMediaItems']
    f=CFUNCTYPE(None,c_uint64,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(selected))
    f(t[0],t[1])
     
def RPR_SelectProjectInstance(proj):
    """
    Python: RPR_SelectProjectInstance(ReaProject proj)
    """
    a=_ft['SelectProjectInstance']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    f(t[0])
     
def RPR_SetActiveTake(take):
    """
    Python: RPR_SetActiveTake(MediaItem_Take take)
    
    set this take active in this media item
    """
    a=_ft['SetActiveTake']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    f(t[0])
     
def RPR_SetAutomationMode(mode,onlySel):
    """
    Python: RPR_SetAutomationMode(Int mode, Boolean onlySel)
    
    sets all or selected tracks to mode.
    """
    a=_ft['SetAutomationMode']
    f=CFUNCTYPE(None,c_int,c_byte)(a)
    t=(c_int(mode),c_byte(onlySel))
    f(t[0],t[1])
     
def RPR_SetCurrentBPM(__proj,bpm,wantUndo):
    """
    Python: RPR_SetCurrentBPM(ReaProject __proj, Float bpm, Boolean wantUndo)
    
    set current BPM in project, set wantUndo=true to add undo point
    """
    a=_ft['SetCurrentBPM']
    f=CFUNCTYPE(None,c_uint64,c_double,c_byte)(a)
    t=(rpr_packp('ReaProject*',__proj),c_double(bpm),c_byte(wantUndo))
    f(t[0],t[1],t[2])
     
def RPR_SetCursorContext(mode,envInOptional):
    """
    Python: RPR_SetCursorContext(Int mode, TrackEnvelope envInOptional)
    
    You must use this to change the focus programmatically. mode=0 to focus track panels, 1 to focus the arrange window, 2 to focus the arrange window and select env (or env==NULL to clear the current track/take envelope selection)
    """
    a=_ft['SetCursorContext']
    f=CFUNCTYPE(None,c_int,c_uint64)(a)
    t=(c_int(mode),rpr_packp('TrackEnvelope*',envInOptional))
    f(t[0],t[1])
     
def RPR_SetEditCurPos(time,moveview,seekplay):
    """
    Python: RPR_SetEditCurPos(Float time, Boolean moveview, Boolean seekplay)
    """
    a=_ft['SetEditCurPos']
    f=CFUNCTYPE(None,c_double,c_byte,c_byte)(a)
    t=(c_double(time),c_byte(moveview),c_byte(seekplay))
    f(t[0],t[1],t[2])
     
def RPR_SetEditCurPos2(proj,time,moveview,seekplay):
    """
    Python: RPR_SetEditCurPos2(ReaProject proj, Float time, Boolean moveview, Boolean seekplay)
    """
    a=_ft['SetEditCurPos2']
    f=CFUNCTYPE(None,c_uint64,c_double,c_byte,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(time),c_byte(moveview),c_byte(seekplay))
    f(t[0],t[1],t[2],t[3])
     
def RPR_SetEnvelopePoint(envelope,ptidx,timeInOptional,valueInOptional,shapeInOptional,tensionInOptional,selectedInOptional,noSortInOptional):
    """
    Python: (Boolean retval, TrackEnvelope envelope, Int ptidx, Float timeInOptional, Float valueInOptional, Int shapeInOptional, Float tensionInOptional, Boolean selectedInOptional, Boolean noSortInOptional) = RPR_SetEnvelopePoint(envelope, ptidx, timeInOptional, valueInOptional, shapeInOptional, tensionInOptional, selectedInOptional, noSortInOptional)
    
    Set attributes of an envelope point. Values that are not supplied will be ignored. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done. See GetEnvelopePoint
    , InsertEnvelopePoint
    , GetEnvelopeScalingMode
    .
    """
    a=_ft['SetEnvelopePoint']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(ptidx),c_double(timeInOptional),c_double(valueInOptional),c_int(shapeInOptional),c_double(tensionInOptional),c_byte(selectedInOptional),c_byte(noSortInOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]))
    return (r,envelope,ptidx,float(t[2].value),float(t[3].value),int(t[4].value),float(t[5].value),int(t[6].value),int(t[7].value))
     
def RPR_SetEnvelopePointEx(envelope,autoitem_idx,ptidx,timeInOptional,valueInOptional,shapeInOptional,tensionInOptional,selectedInOptional,noSortInOptional):
    """
    Python: (Boolean retval, TrackEnvelope envelope, Int autoitem_idx, Int ptidx, Float timeInOptional, Float valueInOptional, Int shapeInOptional, Float tensionInOptional, Boolean selectedInOptional, Boolean noSortInOptional) = RPR_SetEnvelopePointEx(envelope, autoitem_idx, ptidx, timeInOptional, valueInOptional, shapeInOptional, tensionInOptional, selectedInOptional, noSortInOptional)
    
    Set attributes of an envelope point. Values that are not supplied will be ignored. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done. Tautoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePoint
    , InsertEnvelopePoint
    , GetEnvelopeScalingMode
    .
    """
    a=_ft['SetEnvelopePointEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('TrackEnvelope*',envelope),c_int(autoitem_idx),c_int(ptidx),c_double(timeInOptional),c_double(valueInOptional),c_int(shapeInOptional),c_double(tensionInOptional),c_byte(selectedInOptional),c_byte(noSortInOptional))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]),byref(t[7]),byref(t[8]))
    return (r,envelope,autoitem_idx,ptidx,float(t[3].value),float(t[4].value),int(t[5].value),float(t[6].value),int(t[7].value),int(t[8].value))
     
def RPR_SetEnvelopeStateChunk(env,Str,isundoOptional):
    """
    Python: Boolean  RPR_SetEnvelopeStateChunk(TrackEnvelope env, String str, Boolean isundoOptional)
    
    Sets the RPPXML state of an envelope, returns true if successful. Undo flag is a performance/caching hint.
    """
    a=_ft['SetEnvelopeStateChunk']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_byte)(a)
    t=(rpr_packp('TrackEnvelope*',env),rpr_packsc(Str),c_byte(isundoOptional))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetExtState(section,key,value,persist):
    """
    Python: RPR_SetExtState(String section, String key, String value, Boolean persist)
    
    Set the extended state value for a specific section and key. persist=true means the value should be stored and reloaded the next time REAPER is opened. See GetExtState
    , DeleteExtState
    , HasExtState
    .
    """
    a=_ft['SetExtState']
    f=CFUNCTYPE(None,c_char_p,c_char_p,c_char_p,c_byte)(a)
    t=(rpr_packsc(section),rpr_packsc(key),rpr_packsc(value),c_byte(persist))
    f(t[0],t[1],t[2],t[3])
     
def RPR_SetGlobalAutomationOverride(mode):
    """
    Python: RPR_SetGlobalAutomationOverride(Int mode)
    
    mode: see GetGlobalAutomationOverride
    """
    a=_ft['SetGlobalAutomationOverride']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(mode),)
    f(t[0])
     
def RPR_SetItemStateChunk(item,Str,isundoOptional):
    """
    Python: Boolean  RPR_SetItemStateChunk(MediaItem item, String str, Boolean isundoOptional)
    
    Sets the RPPXML state of an item, returns true if successful. Undo flag is a performance/caching hint.
    """
    a=_ft['SetItemStateChunk']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packsc(Str),c_byte(isundoOptional))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetMasterTrackVisibility(flag):
    """
    Python: Int  RPR_SetMasterTrackVisibility(Int flag)
    
    set &1 to show the master track in the TCP, &2 to show in the mixer. Returns the previous visibility state. See GetMasterTrackVisibility
    .
    """
    a=_ft['SetMasterTrackVisibility']
    f=CFUNCTYPE(c_int,c_int)(a)
    t=(c_int(flag),)
    r=f(t[0])
    return r
     
def RPR_SetMediaItemInfo_Value(item,parmname,newvalue):
    """
    Python: Boolean  RPR_SetMediaItemInfo_Value(MediaItem item, String parmname, Float newvalue)
    
    Set media item numerical-value attributes.
    
    B_MUTE : bool * to muted state
    
    B_LOOPSRC : bool * to loop source
    
    B_ALLTAKESPLAY : bool * to all takes play
    
    B_UISEL : bool * to ui selected
    
    C_BEATATTACHMODE : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsosonly
    
    C_LOCK : char * to one char of lock flags (&1 is locked, currently)
    
    D_VOL : double * of item volume (volume bar)
    
    D_POSITION : double * of item position (seconds)
    
    D_LENGTH : double * of item length (seconds)
    
    D_SNAPOFFSET : double * of item snap offset (seconds)
    
    D_FADEINLEN : double * of item fade in length (manual, seconds)
    
    D_FADEOUTLEN : double * of item fade out length (manual, seconds)
    
    D_FADEINDIR : double * of item fade in curve [-1; 1]
    
    D_FADEOUTDIR : double * of item fade out curve [-1; 1]
    
    D_FADEINLEN_AUTO : double * of item autofade in length (seconds, -1 for no autofade set)
    
    D_FADEOUTLEN_AUTO : double * of item autofade out length (seconds, -1 for no autofade set)
    
    C_FADEINSHAPE : int * to fadein shape, 0=linear, ...
    
    C_FADEOUTSHAPE : int * to fadeout shape
    
    I_GROUPID : int * to group ID (0 = no group)
    
    I_LASTY : int * to last y position in track (readonly)
    
    I_LASTH : int * to last height in track (readonly)
    
    I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    
    I_CURTAKE : int * to active take
    
    IP_ITEMNUMBER : int, item number within the track (read-only, returns the item number directly)
    
    F_FREEMODE_Y : float * to free mode y position (0..1)
    
    F_FREEMODE_H : float * to free mode height (0..1)
    """
    a=_ft['SetMediaItemInfo_Value']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_double)(a)
    t=(rpr_packp('MediaItem*',item),rpr_packsc(parmname),c_double(newvalue))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetMediaItemLength(item,length,refreshUI):
    """
    Python: Boolean  RPR_SetMediaItemLength(MediaItem item, Float length, Boolean refreshUI)
    
    Redraws the screen only if refreshUI == true.
    
    See UpdateArrange
    ().
    """
    a=_ft['SetMediaItemLength']
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),c_double(length),c_byte(refreshUI))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetMediaItemPosition(item,position,refreshUI):
    """
    Python: Boolean  RPR_SetMediaItemPosition(MediaItem item, Float position, Boolean refreshUI)
    
    Redraws the screen only if refreshUI == true.
    
    See UpdateArrange
    ().
    """
    a=_ft['SetMediaItemPosition']
    f=CFUNCTYPE(c_byte,c_uint64,c_double,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),c_double(position),c_byte(refreshUI))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetMediaItemSelected(item,selected):
    """
    Python: RPR_SetMediaItemSelected(MediaItem item, Boolean selected)
    """
    a=_ft['SetMediaItemSelected']
    f=CFUNCTYPE(None,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaItem*',item),c_byte(selected))
    f(t[0],t[1])
     
def RPR_SetMediaItemTake_Source(take,source):
    """
    Python: Boolean  RPR_SetMediaItemTake_Source(MediaItem_Take take, PCM_source source)
    
    Set media source of media item take
    """
    a=_ft['SetMediaItemTake_Source']
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packp('PCM_source*',source))
    r=f(t[0],t[1])
    return r
     
def RPR_SetMediaItemTakeInfo_Value(take,parmname,newvalue):
    """
    Python: Boolean  RPR_SetMediaItemTakeInfo_Value(MediaItem_Take take, String parmname, Float newvalue)
    
    Set media item take numerical-value attributes.
    
    D_STARTOFFS : double *, start offset in take of item
    
    D_VOL : double *, take volume
    
    D_PAN : double *, take pan
    
    D_PANLAW : double *, take pan law (-1.0=default, 0.5=-6dB, 1.0=+0dB, etc)
    
    D_PLAYRATE : double *, take playrate (1.0=normal, 2.0=doublespeed, etc)
    
    D_PITCH : double *, take pitch adjust (in semitones, 0.0=normal, +12 = one octave up, etc)
    
    B_PPITCH, bool *, preserve pitch when changing rate
    
    I_CHANMODE, int *, channel mode (0=normal, 1=revstereo, 2=downmix, 3=l, 4=r)
    
    I_PITCHMODE, int *, pitch shifter mode, -1=proj default, otherwise high word=shifter low word = parameter
    
    I_CUSTOMCOLOR : int *, custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    
    IP_TAKENUMBER : int, take number within the item (read-only, returns the take number directly)
    """
    a=_ft['SetMediaItemTakeInfo_Value']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packsc(parmname),c_double(newvalue))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetMediaTrackInfo_Value(tr,parmname,newvalue):
    """
    Python: Boolean  RPR_SetMediaTrackInfo_Value(MediaTrack tr, String parmname, Float newvalue)
    
    Set track numerical-value attributes.
    
    B_MUTE : bool * : mute flag
    
    B_PHASE : bool * : invert track phase
    
    IP_TRACKNUMBER : int : track number (returns zero if not found, -1 for master track) (read-only, returns the int directly)
    
    I_SOLO : int * : 0=not soloed, 1=solo, 2=soloed in place. also: 5=solo-safe solo, 6=solo-safe soloed in place
    
    I_FXEN : int * : 0=fx bypassed, nonzero = fx active
    
    I_RECARM : int * : 0=not record armed, 1=record armed
    
    I_RECINPUT : int * : record input. <0 = no input, 0..n = mono hardware input, 512+n = rearoute input, 1024 set for stereo input pair. 4096 set for MIDI input, if set, then low 5 bits represent channel (0=all, 1-16=only chan), then next 6 bits represent physical input (63=all, 62=VKB)
    
    I_RECMODE : int * : record mode (0=input, 1=stereo out, 2=none, 3=stereo out w/latcomp, 4=midi output, 5=mono out, 6=mono out w/ lat comp, 7=midi overdub, 8=midi replace
    
    I_RECMON : int * : record monitor (0=off, 1=normal, 2=not when playing (tapestyle))
    
    I_RECMONITEMS : int * : monitor items while recording (0=off, 1=on)
    
    I_AUTOMODE : int * : track automation mode (0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
    
    I_NCHAN : int * : number of track channels, must be 2-64, even
    
    I_SELECTED : int * : track selected? 0 or 1
    
    I_WNDH : int * : current TCP window height (Read-only)
    
    I_FOLDERDEPTH : int * : folder depth change (0=normal, 1=track is a folder parent, -1=track is the last in the innermost folder, -2=track is the last in the innermost and next-innermost folders, etc
    
    I_FOLDERCOMPACT : int * : folder compacting (only valid on folders), 0=normal, 1=small, 2=tiny children
    
    I_MIDIHWOUT : int * : track midi hardware output index (<0 for disabled, low 5 bits are which channels (0=all, 1-16), next 5 bits are output device index (0-31))
    
    I_PERFFLAGS : int * : track perf flags (&1=no media buffering, &2=no anticipative FX)
    
    I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    
    I_HEIGHTOVERRIDE : int * : custom height override for TCP window. 0 for none, otherwise size in pixels
    
    B_HEIGHTLOCK : bool * : track height lock (must set I_HEIGHTOVERRIDE before locking)
    
    D_VOL : double * : trim volume of track (0 (-inf)..1 (+0dB) .. 2 (+6dB) etc ..)
    
    D_PAN : double * : trim pan of track (-1..1)
    
    D_WIDTH : double * : width of track (-1..1)
    
    D_DUALPANL : double * : dualpan position 1 (-1..1), only if I_PANMODE==6
    
    D_DUALPANR : double * : dualpan position 2 (-1..1), only if I_PANMODE==6
    
    I_PANMODE : int * : pan mode (0 = classic 3.x, 3=new balance, 5=stereo pan, 6 = dual pan)
    
    D_PANLAW : double * : pan law of track. <0 for project default, 1.0 for +0dB, etc
    
    P_ENV : read only, returns TrackEnvelope *, setNewValue=<VOLENV, <PANENV, etc
    
    B_SHOWINMIXER : bool * : show track panel in mixer -- do not use on master
    
    B_SHOWINTCP : bool * : show track panel in tcp -- do not use on master
    
    B_MAINSEND : bool * : track sends audio to parent
    
    C_MAINSEND_OFFS : char * : track send to parent channel offset
    
    B_FREEMODE : bool * : track free-mode enabled (requires UpdateTimeline() after changing etc)
    
    C_BEATATTACHMODE : char * : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsposonly
    
    F_MCP_FXSEND_SCALE : float * : scale of fx+send area in MCP (0.0=smallest allowed, 1=max allowed)
    
    F_MCP_SENDRGN_SCALE : float * : scale of send area as proportion of the fx+send total area (0=min allow, 1=max)
    """
    a=_ft['SetMediaTrackInfo_Value']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_double)(a)
    t=(rpr_packp('MediaTrack*',tr),rpr_packsc(parmname),c_double(newvalue))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetMIDIEditorGrid(project,division):
    """
    Python: RPR_SetMIDIEditorGrid(ReaProject project, Float division)
    
    Set the MIDI editor grid division. 0.25=quarter note, 1.0/3.0=half note tripet, etc.
    """
    a=_ft['SetMIDIEditorGrid']
    f=CFUNCTYPE(None,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',project),c_double(division))
    f(t[0],t[1])
     
def RPR_SetMixerScroll(leftmosttrack):
    """
    Python: MediaTrack  RPR_SetMixerScroll(MediaTrack leftmosttrack)
    
    Scroll the mixer so that leftmosttrack is the leftmost visible track. Returns the leftmost track after scrolling, which may be different from the passed-in track if there are not enough tracks to its right.
    """
    a=_ft['SetMixerScroll']
    f=CFUNCTYPE(c_uint64,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',leftmosttrack),)
    r=f(t[0])
    return rpr_unpackp('MediaTrack*',r)
     
def RPR_SetMouseModifier(context,modifier_flag,action):
    """
    Python: RPR_SetMouseModifier(String context, Int modifier_flag, String action)
    
    Set the mouse modifier assignment for a specific modifier key assignment, in a specific context.
    
    Context is a string like "MM_CTX_ITEM". Find these strings by modifying an assignment in 
    
    Preferences/Editing/Mouse Modifiers, then looking in reaper-mouse.ini.
    
    Modifier flag is a number from 0 to 15: add 1 for shift, 2 for control, 4 for alt, 8 for win.
    
    (macOS: add 1 for shift, 2 for command, 4 for opt, 8 for control.)
    
    For left-click and double-click contexts, the action can be any built-in command ID number
    
    or any custom action ID string. Find built-in command IDs in the REAPER actions window
    
    (enable "show action IDs" in the context menu), and find custom action ID strings in reaper-kb.ini.
    
    For built-in mouse modifier behaviors, find action IDs (which will be low numbers)
    
    by modifying an assignment in Preferences/Editing/Mouse Modifiers, then looking in reaper-mouse.ini.
    
    Assigning an action of -1 will reset that mouse modifier behavior to factory default.
    
    See GetMouseModifier
    .
    """
    a=_ft['SetMouseModifier']
    f=CFUNCTYPE(None,c_char_p,c_int,c_char_p)(a)
    t=(rpr_packsc(context),c_int(modifier_flag),rpr_packsc(action))
    f(t[0],t[1],t[2])
     
def RPR_SetOnlyTrackSelected(track):
    """
    Python: RPR_SetOnlyTrackSelected(MediaTrack track)
    
    Set exactly one track selected, deselect all others
    """
    a=_ft['SetOnlyTrackSelected']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    f(t[0])
     
def RPR_SetProjectGrid(project,division):
    """
    Python: RPR_SetProjectGrid(ReaProject project, Float division)
    
    Set the arrange view grid division. 0.25=quarter note, 1.0/3.0=half note triplet, etc.
    """
    a=_ft['SetProjectGrid']
    f=CFUNCTYPE(None,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',project),c_double(division))
    f(t[0],t[1])
     
def RPR_SetProjectMarker(markrgnindexnumber,isrgn,pos,rgnend,name):
    """
    Python: Boolean  RPR_SetProjectMarker(Int markrgnindexnumber, Boolean isrgn, Float pos, Float rgnend, String name)
    """
    a=_ft['SetProjectMarker']
    f=CFUNCTYPE(c_byte,c_int,c_byte,c_double,c_double,c_char_p)(a)
    t=(c_int(markrgnindexnumber),c_byte(isrgn),c_double(pos),c_double(rgnend),rpr_packsc(name))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def RPR_SetProjectMarker2(proj,markrgnindexnumber,isrgn,pos,rgnend,name):
    """
    Python: Boolean  RPR_SetProjectMarker2(ReaProject proj, Int markrgnindexnumber, Boolean isrgn, Float pos, Float rgnend, String name)
    """
    a=_ft['SetProjectMarker2']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_double,c_double,c_char_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(markrgnindexnumber),c_byte(isrgn),c_double(pos),c_double(rgnend),rpr_packsc(name))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def RPR_SetProjectMarker3(proj,markrgnindexnumber,isrgn,pos,rgnend,name,color):
    """
    Python: Boolean  RPR_SetProjectMarker3(ReaProject proj, Int markrgnindexnumber, Boolean isrgn, Float pos, Float rgnend, String name, Int color)
    """
    a=_ft['SetProjectMarker3']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_double,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(markrgnindexnumber),c_byte(isrgn),c_double(pos),c_double(rgnend),rpr_packsc(name),c_int(color))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return r
     
def RPR_SetProjectMarker4(proj,markrgnindexnumber,isrgn,pos,rgnend,name,color,flags):
    """
    Python: Boolean  RPR_SetProjectMarker4(ReaProject proj, Int markrgnindexnumber, Boolean isrgn, Float pos, Float rgnend, String name, Int color, Int flags)
    
    color should be 0 to not change, or ColorToNative(r,g,b)|0x1000000, flags&1 to clear name
    """
    a=_ft['SetProjectMarker4']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_double,c_double,c_char_p,c_int,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(markrgnindexnumber),c_byte(isrgn),c_double(pos),c_double(rgnend),rpr_packsc(name),c_int(color),c_int(flags))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7])
    return r
     
def RPR_SetProjectMarkerByIndex(proj,markrgnidx,isrgn,pos,rgnend,IDnumber,name,color):
    """
    Python: Boolean  RPR_SetProjectMarkerByIndex(ReaProject proj, Int markrgnidx, Boolean isrgn, Float pos, Float rgnend, Int IDnumber, String name, Int color)
    
    See SetProjectMarkerByIndex2
    .
    """
    a=_ft['SetProjectMarkerByIndex']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_double,c_double,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(markrgnidx),c_byte(isrgn),c_double(pos),c_double(rgnend),c_int(IDnumber),rpr_packsc(name),c_int(color))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7])
    return r
     
def RPR_SetProjectMarkerByIndex2(proj,markrgnidx,isrgn,pos,rgnend,IDnumber,name,color,flags):
    """
    Python: Boolean  RPR_SetProjectMarkerByIndex2(ReaProject proj, Int markrgnidx, Boolean isrgn, Float pos, Float rgnend, Int IDnumber, String name, Int color, Int flags)
    
    Differs from SetProjectMarker4 in that markrgnidx is 0 for the first marker/region, 1 for the next, etc (see EnumProjectMarkers3
    ), rather than representing the displayed marker/region ID number (see SetProjectMarker3
    ). Function will fail if attempting to set a duplicate ID number for a region (duplicate ID numbers for markers are OK). , flags&1 to clear name.
    """
    a=_ft['SetProjectMarkerByIndex2']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_byte,c_double,c_double,c_int,c_char_p,c_int,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(markrgnidx),c_byte(isrgn),c_double(pos),c_double(rgnend),c_int(IDnumber),rpr_packsc(name),c_int(color),c_int(flags))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8])
    return r
     
def RPR_SetProjExtState(proj,extname,key,value):
    """
    Python: Int  RPR_SetProjExtState(ReaProject proj, String extname, String key, String value)
    
    Save a key/value pair for a specific extension, to be restored the next time this specific project is loaded. Typically extname will be the name of a reascript or extension section. If key is NULL or "", all extended data for that extname will be deleted.  If val is NULL or "", the data previously associated with that key will be deleted. Returns the size of the state for this extname. See GetProjExtState
    , EnumProjExtState
    .
    """
    a=_ft['SetProjExtState']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p,c_char_p,c_char_p)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(extname),rpr_packsc(key),rpr_packsc(value))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_SetRegionRenderMatrix(proj,regionindex,track,addorremove):
    """
    Python: RPR_SetRegionRenderMatrix(ReaProject proj, Int regionindex, MediaTrack track, Int addorremove)
    
    Add (addorremove > 0) or remove (addorremove < 0) a track from this region when using the region render matrix.
    """
    a=_ft['SetRegionRenderMatrix']
    f=CFUNCTYPE(None,c_uint64,c_int,c_uint64,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(regionindex),rpr_packp('MediaTrack*',track),c_int(addorremove))
    f(t[0],t[1],t[2],t[3])
     
def RPR_SetTakeStretchMarker(take,idx,pos,srcposInOptional):
    """
    Python: Int  RPR_SetTakeStretchMarker(MediaItem_Take take, Int idx, Float pos, const double srcposInOptional)
    
    Adds or updates a stretch marker. If idx<0, stretch marker will be added. If idx>=0, stretch marker will be updated. When adding, if srcposInOptional is omitted, source position will be auto-calculated. When updating a stretch marker, if srcposInOptional is omitted, srcpos will not be modified. Position/srcposition values will be constrained to nearby stretch markers. Returns index of stretch marker, or -1 if did not insert (or marker already existed at time).
    """
    a=_ft['SetTakeStretchMarker']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_double,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(idx),c_double(pos),c_double(srcposInOptional))
    r=f(t[0],t[1],t[2],byref(t[3]))
    return (r,take,idx,pos,float(t[3].value))
     
def RPR_SetTakeStretchMarkerSlope(take,idx,slope):
    """
    Python: Boolean  RPR_SetTakeStretchMarkerSlope(MediaItem_Take take, Int idx, Float slope)
    
    See GetTakeStretchMarkerSlope
    """
    a=_ft['SetTakeStretchMarkerSlope']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(idx),c_double(slope))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetTempoTimeSigMarker(proj,ptidx,timepos,measurepos,beatpos,bpm,timesig_num,timesig_denom,lineartempo):
    """
    Python: Boolean  RPR_SetTempoTimeSigMarker(ReaProject proj, Int ptidx, Float timepos, Int measurepos, Float beatpos, Float bpm, Int timesig_num, Int timesig_denom, Boolean lineartempo)
    
    Set parameters of a tempo/time signature marker. Provide either timepos (with measurepos=-1, beatpos=-1), or measurepos and beatpos (with timepos=-1). If timesig_num and timesig_denom are zero, the previous time signature will be used. ptidx=-1 will insert a new tempo/time signature marker. See CountTempoTimeSigMarkers
    , GetTempoTimeSigMarker
    , AddTempoTimeSigMarker
    .
    """
    a=_ft['SetTempoTimeSigMarker']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double,c_int,c_double,c_double,c_int,c_int,c_byte)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(ptidx),c_double(timepos),c_int(measurepos),c_double(beatpos),c_double(bpm),c_int(timesig_num),c_int(timesig_denom),c_byte(lineartempo))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8])
    return r
     
def RPR_SetToggleCommandState(section_id,command_id,state):
    """
    Python: Boolean  RPR_SetToggleCommandState(Int section_id, Int command_id, Int state)
    
    Updates the toggle state of an action, returns true if succeeded. Only ReaScripts can have their toggle states changed programmatically. See RefreshToolbar2
    .
    """
    a=_ft['SetToggleCommandState']
    f=CFUNCTYPE(c_byte,c_int,c_int,c_int)(a)
    t=(c_int(section_id),c_int(command_id),c_int(state))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetTrackAutomationMode(tr,mode):
    """
    Python: RPR_SetTrackAutomationMode(MediaTrack tr, Int mode)
    """
    a=_ft['SetTrackAutomationMode']
    f=CFUNCTYPE(None,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(mode))
    f(t[0],t[1])
     
def RPR_SetTrackColor(track,color):
    """
    Python: RPR_SetTrackColor(MediaTrack track, Int color)
    
    Set the custom track color, color is OS dependent (i.e. ColorToNative(r,g,b).
    """
    a=_ft['SetTrackColor']
    f=CFUNCTYPE(None,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(color))
    f(t[0],t[1])
     
def RPR_SetTrackMIDILyrics(track,flag,Str):
    """
    Python: Boolean  RPR_SetTrackMIDILyrics(MediaTrack track, Int flag, String str)
    
    Set all MIDI lyrics on the track. Lyrics will be stuffed into any MIDI items found in range. Flag is unused at present. str is passed in as beat position, tab, text, tab (example with flag=2: "1.1.2\tLyric for measure 1 beat 2\t.1.1\tLyric for measure 2 beat 1	"). See GetTrackMIDILyrics
    """
    a=_ft['SetTrackMIDILyrics']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(flag),rpr_packsc(Str))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_SetTrackMIDINoteName(track,pitch,chan,name):
    """
    Python: Boolean  RPR_SetTrackMIDINoteName(Int track, Int pitch, Int chan, String name)
    
    channel < 0 assigns these note names to all channels.
    """
    a=_ft['SetTrackMIDINoteName']
    f=CFUNCTYPE(c_byte,c_int,c_int,c_int,c_char_p)(a)
    t=(c_int(track),c_int(pitch),c_int(chan),rpr_packsc(name))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_SetTrackMIDINoteNameEx(proj,track,pitch,chan,name):
    """
    Python: Boolean  RPR_SetTrackMIDINoteNameEx(ReaProject proj, MediaTrack track, Int pitch, Int chan, String name)
    
    channel < 0 assigns note name to all channels. pitch 128 assigns name for CC0, pitch 129 for CC1, etc.
    """
    a=_ft['SetTrackMIDINoteNameEx']
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_int,c_int,c_char_p)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packp('MediaTrack*',track),c_int(pitch),c_int(chan),rpr_packsc(name))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def RPR_SetTrackSelected(track,selected):
    """
    Python: RPR_SetTrackSelected(MediaTrack track, Boolean selected)
    """
    a=_ft['SetTrackSelected']
    f=CFUNCTYPE(None,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_byte(selected))
    f(t[0],t[1])
     
def RPR_SetTrackSendInfo_Value(tr,category,sendidx,parmname,newvalue):
    """
    Python: Boolean  RPR_SetTrackSendInfo_Value(MediaTrack tr, Int category, Int sendidx, String parmname, Float newvalue)
    
    Set send/receive/hardware output numerical-value attributes, return true on success.
    
    category is <0 for receives, 0=sends, >0 for hardware outputs
    
    parameter names:
    
    B_MUTE : returns bool *
    
    B_PHASE : returns bool *, true to flip phase
    
    B_MONO : returns bool *
    
    D_VOL : returns double *, 1.0 = +0dB etc
    
    D_PAN : returns double *, -1..+1
    
    D_PANLAW : returns double *,1.0=+0.0db, 0.5=-6dB, -1.0 = projdef etc
    
    I_SENDMODE : returns int *, 0=post-fader, 1=pre-fx, 2=post-fx (deprecated), 3=post-fx
    
    I_AUTOMODE : returns int * : automation mode (-1=use track automode, 0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
    
    I_SRCCHAN : returns int *, index,&1024=mono, -1 for none
    
    I_DSTCHAN : returns int *, index, &1024=mono, otherwise stereo pair, hwout:&512=rearoute
    
    I_MIDIFLAGS : returns int *, low 5 bits=source channel 0=all, 1-16, next 5 bits=dest channel, 0=orig, 1-16=chanSee CreateTrackSend
    , RemoveTrackSend
    , GetTrackNumSends
    .
    """
    a=_ft['SetTrackSendInfo_Value']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_char_p,c_double)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(category),c_int(sendidx),rpr_packsc(parmname),c_double(newvalue))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def RPR_SetTrackSendUIPan(track,send_idx,pan,isend):
    """
    Python: Boolean  RPR_SetTrackSendUIPan(MediaTrack track, Int send_idx, Float pan, Int isend)
    
    send_idx<0 for receives, >=0 for hw ouputs, >=nb_of_hw_ouputs for sends. isend=1 for end of edit, -1 for an instant edit (such as reset), 0 for normal tweak.
    """
    a=_ft['SetTrackSendUIPan']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(send_idx),c_double(pan),c_int(isend))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_SetTrackSendUIVol(track,send_idx,vol,isend):
    """
    Python: Boolean  RPR_SetTrackSendUIVol(MediaTrack track, Int send_idx, Float vol, Int isend)
    
    send_idx<0 for receives, >=0 for hw ouputs, >=nb_of_hw_ouputs for sends. isend=1 for end of edit, -1 for an instant edit (such as reset), 0 for normal tweak.
    """
    a=_ft['SetTrackSendUIVol']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_double,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(send_idx),c_double(vol),c_int(isend))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_SetTrackStateChunk(track,Str,isundoOptional):
    """
    Python: Boolean  RPR_SetTrackStateChunk(MediaTrack track, String str, Boolean isundoOptional)
    
    Sets the RPPXML state of a track, returns true if successful. Undo flag is a performance/caching hint.
    """
    a=_ft['SetTrackStateChunk']
    f=CFUNCTYPE(c_byte,c_uint64,c_char_p,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packsc(Str),c_byte(isundoOptional))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_ShowActionList(caller,callerWnd):
    """
    Python: RPR_ShowActionList(KbdSectionInfo caller, HWND callerWnd)
    """
    a=_ft['ShowActionList']
    f=CFUNCTYPE(None,c_uint64,c_uint64)(a)
    t=(rpr_packp('KbdSectionInfo*',caller),rpr_packp('HWND',callerWnd))
    f(t[0],t[1])
     
def RPR_ShowConsoleMsg(msg):
    """
    Python: RPR_ShowConsoleMsg(String msg)
    
    Show a message to the user (also useful for debugging). Send "\n" for newline, "" to clear the console. See ClearConsole
    """
    a=_ft['ShowConsoleMsg']
    f=CFUNCTYPE(None,c_char_p)(a)
    t=(rpr_packsc(msg),)
    f(t[0])
     
def RPR_ShowMessageBox(msg,title,Type):
    """
    Python: Int  RPR_ShowMessageBox(String msg, String title, Int type)
    
    type 0=OK,1=OKCANCEL,2=ABORTRETRYIGNORE,3=YESNOCANCEL,4=YESNO,5=RETRYCANCEL : ret 1=OK,2=CANCEL,3=ABORT,4=RETRY,5=IGNORE,6=YES,7=NO
    """
    a=_ft['ShowMessageBox']
    f=CFUNCTYPE(c_int,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packsc(msg),rpr_packsc(title),c_int(Type))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_ShowPopupMenu(name,x,y,hwndParentOptional,ctxOptional,ctx2Optional,ctx3Optional):
    """
    Python: RPR_ShowPopupMenu(String name, Int x, Int y, HWND hwndParentOptional, void ctxOptional, Int ctx2Optional, Int ctx3Optional)
    
    shows a context menu, valid names include: track_input, track_panel, track_area, track_routing, item, ruler, envelope, envelope_point, envelope_item. ctxOptional can be a track pointer for track_*, item pointer for item* (but is optional). for envelope_point, ctx2Optional has point index, ctx3Optional has item index (0=main envelope, 1=first AI). for envelope_item, ctx2Optional has AI index (1=first AI)
    """
    a=_ft['ShowPopupMenu']
    f=CFUNCTYPE(None,c_char_p,c_int,c_int,c_uint64,c_uint64,c_int,c_int)(a)
    t=(rpr_packsc(name),c_int(x),c_int(y),rpr_packp('HWND',hwndParentOptional),rpr_packp('void*',ctxOptional),c_int(ctx2Optional),c_int(ctx3Optional))
    f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
     
def RPR_SLIDER2DB(y):
    """
    Python: Float  RPR_SLIDER2DB(Float y)
    """
    a=_ft['SLIDER2DB']
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(y),)
    r=f(t[0])
    return r
     
def RPR_SnapToGrid(project,time_pos):
    """
    Python: Float  RPR_SnapToGrid(ReaProject project, Float time_pos)
    """
    a=_ft['SnapToGrid']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',project),c_double(time_pos))
    r=f(t[0],t[1])
    return r
     
def RPR_SoloAllTracks(solo):
    """
    Python: RPR_SoloAllTracks(Int solo)
    
    solo=2 for SIP
    """
    a=_ft['SoloAllTracks']
    f=CFUNCTYPE(None,c_int)(a)
    t=(c_int(solo),)
    f(t[0])
     
def RPR_Splash_GetWnd():
    """
    Python: HWND  RPR_Splash_GetWnd()
    
    gets the splash window, in case you want to display a message over it. Returns NULL when the sphah window is not displayed.
    """
    a=_ft['Splash_GetWnd']
    f=CFUNCTYPE(c_uint64)(a)
    r=f()
    return rpr_unpackp('HWND',r)
     
def RPR_SplitMediaItem(item,position):
    """
    Python: MediaItem  RPR_SplitMediaItem(MediaItem item, Float position)
    
    the original item becomes the left-hand split, the function returns the right-hand split (or NULL if the split failed)
    """
    a=_ft['SplitMediaItem']
    f=CFUNCTYPE(c_uint64,c_uint64,c_double)(a)
    t=(rpr_packp('MediaItem*',item),c_double(position))
    r=f(t[0],t[1])
    return rpr_unpackp('MediaItem*',r)
     
def RPR_stringToGuid(Str,g):
    """
    Python: RPR_stringToGuid(String str, GUID g)
    """
    a=_ft['stringToGuid']
    f=CFUNCTYPE(None,c_char_p,c_uint64)(a)
    t=(rpr_packsc(Str),rpr_packp('GUID*',g))
    f(t[0],t[1])
     
def RPR_StuffMIDIMessage(mode,msg1,msg2,msg3):
    """
    Python: RPR_StuffMIDIMessage(Int mode, Int msg1, Int msg2, Int msg3)
    
    Stuffs a 3 byte MIDI message into either the Virtual MIDI Keyboard queue, or the MIDI-as-control input queue, or sends to a MIDI hardware output. mode=0 for VKB, 1 for control (actions map etc), 2 for VKB-on-current-channel; 16 for external MIDI device 0, 17 for external MIDI device 1, etc; see GetNumMIDIOutputs
    , GetMIDIOutputName
    .
    """
    a=_ft['StuffMIDIMessage']
    f=CFUNCTYPE(None,c_int,c_int,c_int,c_int)(a)
    t=(c_int(mode),c_int(msg1),c_int(msg2),c_int(msg3))
    f(t[0],t[1],t[2],t[3])
     
def RPR_TakeFX_AddByName(take,fxname,instantiate):
    """
    Python: Int  RPR_TakeFX_AddByName(MediaItem_Take take, String fxname, Int instantiate)
    
    Adds or queries the position of a named FX in a take. Specify a negative value for instantiate to always create a new effect, 0 to only query the first instance of an effect, or a positive value to add an instance if one is not found.
    """
    a=_ft['TakeFX_AddByName']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),rpr_packsc(fxname),c_int(instantiate))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TakeFX_CopyToTake(src_take,src_fx,dest_take,dest_fx,is_move):
    """
    Python: RPR_TakeFX_CopyToTake(MediaItem_Take src_take, Int src_fx, MediaItem_Take dest_take, Int dest_fx, Boolean is_move)
    
    Copies (or moves) FX from src_take to dest_take. Can be used with src_track=dest_track to reorder.
    """
    a=_ft['TakeFX_CopyToTake']
    f=CFUNCTYPE(None,c_uint64,c_int,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',src_take),c_int(src_fx),rpr_packp('MediaItem_Take*',dest_take),c_int(dest_fx),c_byte(is_move))
    f(t[0],t[1],t[2],t[3],t[4])
     
def RPR_TakeFX_CopyToTrack(src_take,src_fx,dest_track,dest_fx,is_move):
    """
    Python: RPR_TakeFX_CopyToTrack(MediaItem_Take src_take, Int src_fx, MediaTrack dest_track, Int dest_fx, Boolean is_move)
    
    Copies (or moves) FX from src_take to dest_track. dest_fx can have 0x1000000 set to reference input FX.
    """
    a=_ft['TakeFX_CopyToTrack']
    f=CFUNCTYPE(None,c_uint64,c_int,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',src_take),c_int(src_fx),rpr_packp('MediaTrack*',dest_track),c_int(dest_fx),c_byte(is_move))
    f(t[0],t[1],t[2],t[3],t[4])
     
def RPR_TakeFX_Delete(take,fx):
    """
    Python: Boolean  RPR_TakeFX_Delete(MediaItem_Take take, Int fx)
    
    Remove a FX from take chain (returns true on success)
    """
    a=_ft['TakeFX_Delete']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TakeFX_EndParamEdit(take,fx,param):
    """
    Python: Boolean  RPR_TakeFX_EndParamEdit(MediaItem_Take take, Int fx, Int param)
    """
    a=_ft['TakeFX_EndParamEdit']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TakeFX_FormatParamValue(take,fx,param,val,buf,buf_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, Int param, Float val, String buf, Int buf_sz) = RPR_TakeFX_FormatParamValue(take, fx, param, val, buf, buf_sz)
    
    Note: only works with FX that support Cockos VST extensions.
    """
    a=_ft['TakeFX_FormatParamValue']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),c_double(val),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return (r,take,fx,param,val,rpr_unpacks(t[4]),buf_sz)
     
def RPR_TakeFX_FormatParamValueNormalized(take,fx,param,value,buf,buf_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, Int param, Float value, String buf, Int buf_sz) = RPR_TakeFX_FormatParamValueNormalized(take, fx, param, value, buf, buf_sz)
    
    Note: only works with FX that support Cockos VST extensions.
    """
    a=_ft['TakeFX_FormatParamValueNormalized']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),c_double(value),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return (r,take,fx,param,value,rpr_unpacks(t[4]),buf_sz)
     
def RPR_TakeFX_GetChainVisible(take):
    """
    Python: Int  RPR_TakeFX_GetChainVisible(MediaItem_Take take)
    
    returns index of effect visible in chain, or -1 for chain hidden, or -2 for chain visible but no effect selected
    """
    a=_ft['TakeFX_GetChainVisible']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def RPR_TakeFX_GetCount(take):
    """
    Python: Int  RPR_TakeFX_GetCount(MediaItem_Take take)
    """
    a=_ft['TakeFX_GetCount']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def RPR_TakeFX_GetEnabled(take,fx):
    """
    Python: Boolean  RPR_TakeFX_GetEnabled(MediaItem_Take take, Int fx)
    
    See TakeFX_SetEnabled
    """
    a=_ft['TakeFX_GetEnabled']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TakeFX_GetEnvelope(take,fxindex,parameterindex,create):
    """
    Python: TrackEnvelope  RPR_TakeFX_GetEnvelope(MediaItem_Take take, Int fxindex, Int parameterindex, Boolean create)
    
    Returns the FX parameter envelope. If the envelope does not exist and create=true, the envelope will be created.
    """
    a=_ft['TakeFX_GetEnvelope']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fxindex),c_int(parameterindex),c_byte(create))
    r=f(t[0],t[1],t[2],t[3])
    return rpr_unpackp('TrackEnvelope*',r)
     
def RPR_TakeFX_GetFloatingWindow(take,index):
    """
    Python: HWND  RPR_TakeFX_GetFloatingWindow(MediaItem_Take take, Int index)
    
    returns HWND of floating window for effect index, if any
    """
    a=_ft['TakeFX_GetFloatingWindow']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(index))
    r=f(t[0],t[1])
    return rpr_unpackp('HWND',r)
     
def RPR_TakeFX_GetFormattedParamValue(take,fx,param,buf,buf_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, Int param, String buf, Int buf_sz) = RPR_TakeFX_GetFormattedParamValue(take, fx, param, buf, buf_sz)
    """
    a=_ft['TakeFX_GetFormattedParamValue']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,take,fx,param,rpr_unpacks(t[3]),buf_sz)
     
def RPR_TakeFX_GetFXGUID(take,fx):
    """
    Python: GUID  RPR_TakeFX_GetFXGUID(MediaItem_Take take, Int fx)
    """
    a=_ft['TakeFX_GetFXGUID']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx))
    r=f(t[0],t[1])
    return rpr_unpackp('GUID*',r)
     
def RPR_TakeFX_GetFXName(take,fx,buf,buf_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, String buf, Int buf_sz) = RPR_TakeFX_GetFXName(take, fx, buf, buf_sz)
    """
    a=_ft['TakeFX_GetFXName']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,take,fx,rpr_unpacks(t[2]),buf_sz)
     
def RPR_TakeFX_GetIOSize(take,fx,inputPinsOutOptional,outputPinsOutOptional):
    """
    Python: (Int retval, MediaItem_Take take, Int fx, Int inputPinsOutOptional, Int outputPinsOutOptional) = RPR_TakeFX_GetIOSize(take, fx, inputPinsOutOptional, outputPinsOutOptional)
    
    sets the number of input/output pins for FX if available, returns plug-in type or -1 on error
    """
    a=_ft['TakeFX_GetIOSize']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(inputPinsOutOptional),c_int(outputPinsOutOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (r,take,fx,int(t[2].value),int(t[3].value))
     
def RPR_TakeFX_GetNamedConfigParm(take,fx,parmname,bufOut,bufOut_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, String parmname, String bufOut, Int bufOut_sz) = RPR_TakeFX_GetNamedConfigParm(take, fx, parmname, bufOut, bufOut_sz)
    
    gets plug-in specific named configuration value (returns true on success). see TrackFX_GetNamedConfigParm
    """
    a=_ft['TakeFX_GetNamedConfigParm']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),rpr_packsc(parmname),rpr_packs(bufOut),c_int(bufOut_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,take,fx,parmname,rpr_unpacks(t[3]),bufOut_sz)
     
def RPR_TakeFX_GetNumParams(take,fx):
    """
    Python: Int  RPR_TakeFX_GetNumParams(MediaItem_Take take, Int fx)
    """
    a=_ft['TakeFX_GetNumParams']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TakeFX_GetOffline(take,fx):
    """
    Python: Boolean  RPR_TakeFX_GetOffline(MediaItem_Take take, Int fx)
    
    See TakeFX_SetOffline
    """
    a=_ft['TakeFX_GetOffline']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TakeFX_GetOpen(take,fx):
    """
    Python: Boolean  RPR_TakeFX_GetOpen(MediaItem_Take take, Int fx)
    
    Returns true if this FX UI is open in the FX chain window or a floating window. See TakeFX_SetOpen
    """
    a=_ft['TakeFX_GetOpen']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TakeFX_GetParam(take,fx,param,minvalOut,maxvalOut):
    """
    Python: (Float retval, MediaItem_Take take, Int fx, Int param, Float minvalOut, Float maxvalOut) = RPR_TakeFX_GetParam(take, fx, param, minvalOut, maxvalOut)
    """
    a=_ft['TakeFX_GetParam']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),c_double(minvalOut),c_double(maxvalOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]))
    return (r,take,fx,param,float(t[3].value),float(t[4].value))
     
def RPR_TakeFX_GetParameterStepSizes(take,fx,param,stepOut,smallstepOut,largestepOut,istoggleOut):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, Int param, Float stepOut, Float smallstepOut, Float largestepOut, Boolean istoggleOut) = RPR_TakeFX_GetParameterStepSizes(take, fx, param, stepOut, smallstepOut, largestepOut, istoggleOut)
    """
    a=_ft['TakeFX_GetParameterStepSizes']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),c_double(stepOut),c_double(smallstepOut),c_double(largestepOut),c_byte(istoggleOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]))
    return (r,take,fx,param,float(t[3].value),float(t[4].value),float(t[5].value),int(t[6].value))
     
def RPR_TakeFX_GetParamEx(take,fx,param,minvalOut,maxvalOut,midvalOut):
    """
    Python: (Float retval, MediaItem_Take take, Int fx, Int param, Float minvalOut, Float maxvalOut, Float midvalOut) = RPR_TakeFX_GetParamEx(take, fx, param, minvalOut, maxvalOut, midvalOut)
    """
    a=_ft['TakeFX_GetParamEx']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),c_double(minvalOut),c_double(maxvalOut),c_double(midvalOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),byref(t[5]))
    return (r,take,fx,param,float(t[3].value),float(t[4].value),float(t[5].value))
     
def RPR_TakeFX_GetParamName(take,fx,param,buf,buf_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, Int param, String buf, Int buf_sz) = RPR_TakeFX_GetParamName(take, fx, param, buf, buf_sz)
    """
    a=_ft['TakeFX_GetParamName']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,take,fx,param,rpr_unpacks(t[3]),buf_sz)
     
def RPR_TakeFX_GetParamNormalized(take,fx,param):
    """
    Python: Float  RPR_TakeFX_GetParamNormalized(MediaItem_Take take, Int fx, Int param)
    """
    a=_ft['TakeFX_GetParamNormalized']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TakeFX_GetPinMappings(tr,fx,isoutput,pin,high32OutOptional):
    """
    Python: (Int retval, MediaItem_Take tr, Int fx, Int isoutput, Int pin, Int high32OutOptional) = RPR_TakeFX_GetPinMappings(tr, fx, isoutput, pin, high32OutOptional)
    
    gets the effective channel mapping bitmask for a particular pin. high32OutOptional will be set to the high 32 bits
    """
    a=_ft['TakeFX_GetPinMappings']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_int,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',tr),c_int(fx),c_int(isoutput),c_int(pin),c_int(high32OutOptional))
    r=f(t[0],t[1],t[2],t[3],byref(t[4]))
    return (r,tr,fx,isoutput,pin,int(t[4].value))
     
def RPR_TakeFX_GetPreset(take,fx,presetname,presetname_sz):
    """
    Python: (Boolean retval, MediaItem_Take take, Int fx, String presetname, Int presetname_sz) = RPR_TakeFX_GetPreset(take, fx, presetname, presetname_sz)
    
    Get the name of the preset currently showing in the REAPER dropdown, or the full path to a factory preset file for VST3 plug-ins (.vstpreset). Returns false if the current FX parameters do not exactly match the preset (in other words, if the user loaded the preset but moved the knobs afterward). See TakeFX_SetPreset
    .
    """
    a=_ft['TakeFX_GetPreset']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),rpr_packs(presetname),c_int(presetname_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,take,fx,rpr_unpacks(t[2]),presetname_sz)
     
def RPR_TakeFX_GetPresetIndex(take,fx,numberOfPresetsOut):
    """
    Python: (Int retval, MediaItem_Take take, Int fx, Int numberOfPresetsOut) = RPR_TakeFX_GetPresetIndex(take, fx, numberOfPresetsOut)
    
    Returns current preset index, or -1 if error. numberOfPresetsOut will be set to total number of presets available. See TakeFX_SetPresetByIndex
    """
    a=_ft['TakeFX_GetPresetIndex']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(numberOfPresetsOut))
    r=f(t[0],t[1],byref(t[2]))
    return (r,take,fx,int(t[2].value))
     
def RPR_TakeFX_GetUserPresetFilename(take,fx,fn,fn_sz):
    """
    Python: (MediaItem_Take take, Int fx, String fn, Int fn_sz) = RPR_TakeFX_GetUserPresetFilename(take, fx, fn, fn_sz)
    """
    a=_ft['TakeFX_GetUserPresetFilename']
    f=CFUNCTYPE(None,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),rpr_packs(fn),c_int(fn_sz))
    f(t[0],t[1],t[2],t[3])
    return (take,fx,rpr_unpacks(t[2]),fn_sz)
     
def RPR_TakeFX_NavigatePresets(take,fx,presetmove):
    """
    Python: Boolean  RPR_TakeFX_NavigatePresets(MediaItem_Take take, Int fx, Int presetmove)
    
    presetmove==1 activates the next preset, presetmove==-1 activates the previous preset, etc.
    """
    a=_ft['TakeFX_NavigatePresets']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(presetmove))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TakeFX_SetEnabled(take,fx,enabled):
    """
    Python: RPR_TakeFX_SetEnabled(MediaItem_Take take, Int fx, Boolean enabled)
    
    See TakeFX_GetEnabled
    """
    a=_ft['TakeFX_SetEnabled']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_byte(enabled))
    f(t[0],t[1],t[2])
     
def RPR_TakeFX_SetNamedConfigParm(take,fx,parmname,value):
    """
    Python: Boolean  RPR_TakeFX_SetNamedConfigParm(MediaItem_Take take, Int fx, String parmname, String value)
    
    gets plug-in specific named configuration value (returns true on success)
    """
    a=_ft['TakeFX_SetNamedConfigParm']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_char_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),rpr_packsc(parmname),rpr_packsc(value))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TakeFX_SetOffline(take,fx,offline):
    """
    Python: RPR_TakeFX_SetOffline(MediaItem_Take take, Int fx, Boolean offline)
    
    See TakeFX_GetOffline
    """
    a=_ft['TakeFX_SetOffline']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_byte(offline))
    f(t[0],t[1],t[2])
     
def RPR_TakeFX_SetOpen(take,fx,Open):
    """
    Python: RPR_TakeFX_SetOpen(MediaItem_Take take, Int fx, Boolean open)
    
    Open this FX UI. See TakeFX_GetOpen
    """
    a=_ft['TakeFX_SetOpen']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_byte(Open))
    f(t[0],t[1],t[2])
     
def RPR_TakeFX_SetParam(take,fx,param,val):
    """
    Python: Boolean  RPR_TakeFX_SetParam(MediaItem_Take take, Int fx, Int param, Float val)
    """
    a=_ft['TakeFX_SetParam']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),c_double(val))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TakeFX_SetParamNormalized(take,fx,param,value):
    """
    Python: Boolean  RPR_TakeFX_SetParamNormalized(MediaItem_Take take, Int fx, Int param, Float value)
    """
    a=_ft['TakeFX_SetParamNormalized']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(param),c_double(value))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TakeFX_SetPinMappings(tr,fx,isoutput,pin,low32bits,hi32bits):
    """
    Python: Boolean  RPR_TakeFX_SetPinMappings(MediaItem_Take tr, Int fx, Int isoutput, Int pin, Int low32bits, Int hi32bits)
    
    sets the channel mapping bitmask for a particular pin. returns false if unsupported (not all types of plug-ins support this capability)
    """
    a=_ft['TakeFX_SetPinMappings']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_int,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',tr),c_int(fx),c_int(isoutput),c_int(pin),c_int(low32bits),c_int(hi32bits))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def RPR_TakeFX_SetPreset(take,fx,presetname):
    """
    Python: Boolean  RPR_TakeFX_SetPreset(MediaItem_Take take, Int fx, String presetname)
    
    Activate a preset with the name shown in the REAPER dropdown. Full paths to .vstpreset files are also supported for VST3 plug-ins. See TakeFX_GetPreset
    .
    """
    a=_ft['TakeFX_SetPreset']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),rpr_packsc(presetname))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TakeFX_SetPresetByIndex(take,fx,idx):
    """
    Python: Boolean  RPR_TakeFX_SetPresetByIndex(MediaItem_Take take, Int fx, Int idx)
    
    Sets the preset idx, or the factory preset (idx==-2), or the default user preset (idx==-1). Returns true on success. See TakeFX_GetPresetIndex
    .
    """
    a=_ft['TakeFX_SetPresetByIndex']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(fx),c_int(idx))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TakeFX_Show(take,index,showFlag):
    """
    Python: RPR_TakeFX_Show(MediaItem_Take take, Int index, Int showFlag)
    
    showflag=0 for hidechain, =1 for show chain(index valid), =2 for hide floating window(index valid), =3 for show floating window (index valid)
    """
    a=_ft['TakeFX_Show']
    f=CFUNCTYPE(None,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaItem_Take*',take),c_int(index),c_int(showFlag))
    f(t[0],t[1],t[2])
     
def RPR_TakeIsMIDI(take):
    """
    Python: Boolean  RPR_TakeIsMIDI(MediaItem_Take take)
    
    Returns true if the active take contains MIDI.
    """
    a=_ft['TakeIsMIDI']
    f=CFUNCTYPE(c_byte,c_uint64)(a)
    t=(rpr_packp('MediaItem_Take*',take),)
    r=f(t[0])
    return r
     
def RPR_time_precise():
    """
    Python: Float  RPR_time_precise()
    
    Gets a precise system timestamp in seconds
    """
    a=_ft['time_precise']
    f=CFUNCTYPE(c_double)(a)
    r=f()
    return r
     
def RPR_TimeMap2_beatsToTime(proj,tpos,measuresInOptional):
    """
    Python: Float  RPR_TimeMap2_beatsToTime(ReaProject proj, Float tpos, const int measuresInOptional)
    
    convert a beat position (or optionally a beats+measures if measures is non-NULL) to time.
    """
    a=_ft['TimeMap2_beatsToTime']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(tpos),c_int(measuresInOptional))
    r=f(t[0],t[1],byref(t[2]))
    return (r,proj,tpos,int(t[2].value))
     
def RPR_TimeMap2_GetDividedBpmAtTime(proj,time):
    """
    Python: Float  RPR_TimeMap2_GetDividedBpmAtTime(ReaProject proj, Float time)
    
    get the effective BPM at the time (seconds) position (i.e. 2x in /8 signatures)
    """
    a=_ft['TimeMap2_GetDividedBpmAtTime']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(time))
    r=f(t[0],t[1])
    return r
     
def RPR_TimeMap2_GetNextChangeTime(proj,time):
    """
    Python: Float  RPR_TimeMap2_GetNextChangeTime(ReaProject proj, Float time)
    
    when does the next time map (tempo or time sig) change occur
    """
    a=_ft['TimeMap2_GetNextChangeTime']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(time))
    r=f(t[0],t[1])
    return r
     
def RPR_TimeMap2_QNToTime(proj,qn):
    """
    Python: Float  RPR_TimeMap2_QNToTime(ReaProject proj, Float qn)
    
    converts project QN position to time.
    """
    a=_ft['TimeMap2_QNToTime']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(qn))
    r=f(t[0],t[1])
    return r
     
def RPR_TimeMap2_timeToBeats(proj,tpos,measuresOutOptional,cmlOutOptional,fullbeatsOutOptional,cdenomOutOptional):
    """
    Python: (Float retval, ReaProject proj, Float tpos, Int measuresOutOptional, Int cmlOutOptional, Float fullbeatsOutOptional, Int cdenomOutOptional) = RPR_TimeMap2_timeToBeats(proj, tpos, measuresOutOptional, cmlOutOptional, fullbeatsOutOptional, cdenomOutOptional)
    
    convert a time into beats.
    
    if measures is non-NULL, measures will be set to the measure count, return value will be beats since measure.
    
    if cml is non-NULL, will be set to current measure length in beats (i.e. time signature numerator)
    
    if fullbeats is non-NULL, and measures is non-NULL, fullbeats will get the full beat count (same value returned if measures is NULL).
    
    if cdenom is non-NULL, will be set to the current time signature denominator.
    """
    a=_ft['TimeMap2_timeToBeats']
    f=CFUNCTYPE(c_double,c_uint64,c_double,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(tpos),c_int(measuresOutOptional),c_int(cmlOutOptional),c_double(fullbeatsOutOptional),c_int(cdenomOutOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]))
    return (r,proj,tpos,int(t[2].value),int(t[3].value),float(t[4].value),int(t[5].value))
     
def RPR_TimeMap2_timeToQN(proj,tpos):
    """
    Python: Float  RPR_TimeMap2_timeToQN(ReaProject proj, Float tpos)
    
    converts project time position to QN position.
    """
    a=_ft['TimeMap2_timeToQN']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(tpos))
    r=f(t[0],t[1])
    return r
     
def RPR_TimeMap_curFrameRate(proj,dropFrameOutOptional):
    """
    Python: (Float retval, ReaProject proj, Boolean dropFrameOutOptional) = RPR_TimeMap_curFrameRate(proj, dropFrameOutOptional)
    
    Gets project framerate, and optionally whether it is drop-frame timecode
    """
    a=_ft['TimeMap_curFrameRate']
    f=CFUNCTYPE(c_double,c_uint64,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_byte(dropFrameOutOptional))
    r=f(t[0],byref(t[1]))
    return (r,proj,int(t[1].value))
     
def RPR_TimeMap_GetDividedBpmAtTime(time):
    """
    Python: Float  RPR_TimeMap_GetDividedBpmAtTime(Float time)
    
    get the effective BPM at the time (seconds) position (i.e. 2x in /8 signatures)
    """
    a=_ft['TimeMap_GetDividedBpmAtTime']
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(time),)
    r=f(t[0])
    return r
     
def RPR_TimeMap_GetMeasureInfo(proj,measure,qn_startOut,qn_endOut,timesig_numOut,timesig_denomOut,tempoOut):
    """
    Python: (Float retval, ReaProject proj, Int measure, Float qn_startOut, Float qn_endOut, Int timesig_numOut, Int timesig_denomOut, Float tempoOut) = RPR_TimeMap_GetMeasureInfo(proj, measure, qn_startOut, qn_endOut, timesig_numOut, timesig_denomOut, tempoOut)
    
    Get the QN position and time signature information for the start of a measure. Return the time in seconds of the measure start.
    """
    a=_ft['TimeMap_GetMeasureInfo']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_void_p,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_int(measure),c_double(qn_startOut),c_double(qn_endOut),c_int(timesig_numOut),c_int(timesig_denomOut),c_double(tempoOut))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]))
    return (r,proj,measure,float(t[2].value),float(t[3].value),int(t[4].value),int(t[5].value),float(t[6].value))
     
def RPR_TimeMap_GetMetronomePattern(proj,time,pattern,pattern_sz):
    """
    Python: (Int retval, ReaProject proj, Float time, String pattern, Int pattern_sz) = RPR_TimeMap_GetMetronomePattern(proj, time, pattern, pattern_sz)
    
    Fills in a string representing the active metronome pattern. For example, in a 7/8 measure divided 3+4, the pattern might be "1221222". The length of the string is the time signature numerator, and the function returns the time signature denominator.
    """
    a=_ft['TimeMap_GetMetronomePattern']
    f=CFUNCTYPE(c_int,c_uint64,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(time),rpr_packs(pattern),c_int(pattern_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,proj,time,rpr_unpacks(t[2]),pattern_sz)
     
def RPR_TimeMap_GetTimeSigAtTime(proj,time,timesig_numOut,timesig_denomOut,tempoOut):
    """
    Python: (ReaProject proj, Float time, Int timesig_numOut, Int timesig_denomOut, Float tempoOut) = RPR_TimeMap_GetTimeSigAtTime(proj, time, timesig_numOut, timesig_denomOut, tempoOut)
    
    get the effective time signature and tempo
    """
    a=_ft['TimeMap_GetTimeSigAtTime']
    f=CFUNCTYPE(None,c_uint64,c_double,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(time),c_int(timesig_numOut),c_int(timesig_denomOut),c_double(tempoOut))
    f(t[0],t[1],byref(t[2]),byref(t[3]),byref(t[4]))
    return (proj,time,int(t[2].value),int(t[3].value),float(t[4].value))
     
def RPR_TimeMap_QNToMeasures(proj,qn,qnMeasureStartOutOptional,qnMeasureEndOutOptional):
    """
    Python: (Int retval, ReaProject proj, Float qn, Float qnMeasureStartOutOptional, Float qnMeasureEndOutOptional) = RPR_TimeMap_QNToMeasures(proj, qn, qnMeasureStartOutOptional, qnMeasureEndOutOptional)
    
    Find which measure the given QN position falls in.
    """
    a=_ft['TimeMap_QNToMeasures']
    f=CFUNCTYPE(c_int,c_uint64,c_double,c_void_p,c_void_p)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(qn),c_double(qnMeasureStartOutOptional),c_double(qnMeasureEndOutOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (r,proj,qn,float(t[2].value),float(t[3].value))
     
def RPR_TimeMap_QNToTime(qn):
    """
    Python: Float  RPR_TimeMap_QNToTime(Float qn)
    
    converts project QN position to time.
    """
    a=_ft['TimeMap_QNToTime']
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(qn),)
    r=f(t[0])
    return r
     
def RPR_TimeMap_QNToTime_abs(proj,qn):
    """
    Python: Float  RPR_TimeMap_QNToTime_abs(ReaProject proj, Float qn)
    
    Converts project quarter note count (QN) to time. QN is counted from the start of the project, regardless of any partial measures. See TimeMap2_QNToTime
    """
    a=_ft['TimeMap_QNToTime_abs']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(qn))
    r=f(t[0],t[1])
    return r
     
def RPR_TimeMap_timeToQN(tpos):
    """
    Python: Float  RPR_TimeMap_timeToQN(Float tpos)
    
    converts project QN position to time.
    """
    a=_ft['TimeMap_timeToQN']
    f=CFUNCTYPE(c_double,c_double)(a)
    t=(c_double(tpos),)
    r=f(t[0])
    return r
     
def RPR_TimeMap_timeToQN_abs(proj,tpos):
    """
    Python: Float  RPR_TimeMap_timeToQN_abs(ReaProject proj, Float tpos)
    
    Converts project time position to quarter note count (QN). QN is counted from the start of the project, regardless of any partial measures. See TimeMap2_timeToQN
    """
    a=_ft['TimeMap_timeToQN_abs']
    f=CFUNCTYPE(c_double,c_uint64,c_double)(a)
    t=(rpr_packp('ReaProject*',proj),c_double(tpos))
    r=f(t[0],t[1])
    return r
     
def RPR_ToggleTrackSendUIMute(track,send_idx):
    """
    Python: Boolean  RPR_ToggleTrackSendUIMute(MediaTrack track, Int send_idx)
    
    send_idx<0 for receives, >=0 for hw ouputs, >=nb_of_hw_ouputs for sends.
    """
    a=_ft['ToggleTrackSendUIMute']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(send_idx))
    r=f(t[0],t[1])
    return r
     
def RPR_Track_GetPeakHoldDB(track,channel,clear):
    """
    Python: Float  RPR_Track_GetPeakHoldDB(MediaTrack track, Int channel, Boolean clear)
    """
    a=_ft['Track_GetPeakHoldDB']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(channel),c_byte(clear))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_Track_GetPeakInfo(track,channel):
    """
    Python: Float  RPR_Track_GetPeakInfo(MediaTrack track, Int channel)
    """
    a=_ft['Track_GetPeakInfo']
    f=CFUNCTYPE(c_double,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(channel))
    r=f(t[0],t[1])
    return r
     
def RPR_TrackCtl_SetToolTip(fmt,xpos,ypos,topmost):
    """
    Python: RPR_TrackCtl_SetToolTip(String fmt, Int xpos, Int ypos, Boolean topmost)
    
    displays tooltip at location, or removes if empty string
    """
    a=_ft['TrackCtl_SetToolTip']
    f=CFUNCTYPE(None,c_char_p,c_int,c_int,c_byte)(a)
    t=(rpr_packsc(fmt),c_int(xpos),c_int(ypos),c_byte(topmost))
    f(t[0],t[1],t[2],t[3])
     
def RPR_TrackFX_AddByName(track,fxname,recFX,instantiate):
    """
    Python: Int  RPR_TrackFX_AddByName(MediaTrack track, String fxname, Boolean recFX, Int instantiate)
    
    Adds or queries the position of a named FX from the track FX chain (recFX=false) or record input FX/monitoring FX (recFX=true, monitoring FX are on master track). Specify a negative value for instantiate to always create a new effect, 0 to only query the first instance of an effect, or a positive value to add an instance if one is not found. fxname can have prefix to specify type: VST3:,VST2:,VST:,AU:,JS:, or DX:.
    """
    a=_ft['TrackFX_AddByName']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p,c_byte,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packsc(fxname),c_byte(recFX),c_int(instantiate))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TrackFX_CopyToTake(src_track,src_fx,dest_take,dest_fx,is_move):
    """
    Python: RPR_TrackFX_CopyToTake(MediaTrack src_track, Int src_fx, MediaItem_Take dest_take, Int dest_fx, Boolean is_move)
    
    Copies (or moves) FX from src_track to dest_take. src_fx can have 0x1000000 set to reference input FX.
    """
    a=_ft['TrackFX_CopyToTake']
    f=CFUNCTYPE(None,c_uint64,c_int,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',src_track),c_int(src_fx),rpr_packp('MediaItem_Take*',dest_take),c_int(dest_fx),c_byte(is_move))
    f(t[0],t[1],t[2],t[3],t[4])
     
def RPR_TrackFX_CopyToTrack(src_track,src_fx,dest_track,dest_fx,is_move):
    """
    Python: RPR_TrackFX_CopyToTrack(MediaTrack src_track, Int src_fx, MediaTrack dest_track, Int dest_fx, Boolean is_move)
    
    Copies (or moves) FX from src_track to dest_track. Can be used with src_track=dest_track to reorder, FX indices have 0x1000000 set to reference input FX.
    """
    a=_ft['TrackFX_CopyToTrack']
    f=CFUNCTYPE(None,c_uint64,c_int,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',src_track),c_int(src_fx),rpr_packp('MediaTrack*',dest_track),c_int(dest_fx),c_byte(is_move))
    f(t[0],t[1],t[2],t[3],t[4])
     
def RPR_TrackFX_Delete(track,fx):
    """
    Python: Boolean  RPR_TrackFX_Delete(MediaTrack track, Int fx)
    
    Remove a FX from track chain (returns true on success)
    """
    a=_ft['TrackFX_Delete']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TrackFX_EndParamEdit(track,fx,param):
    """
    Python: Boolean  RPR_TrackFX_EndParamEdit(MediaTrack track, Int fx, Int param)
    """
    a=_ft['TrackFX_EndParamEdit']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TrackFX_FormatParamValue(track,fx,param,val,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, Int param, Float val, String buf, Int buf_sz) = RPR_TrackFX_FormatParamValue(track, fx, param, val, buf, buf_sz)
    
    Note: only works with FX that support Cockos VST extensions.
    """
    a=_ft['TrackFX_FormatParamValue']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),c_double(val),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return (r,track,fx,param,val,rpr_unpacks(t[4]),buf_sz)
     
def RPR_TrackFX_FormatParamValueNormalized(track,fx,param,value,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, Int param, Float value, String buf, Int buf_sz) = RPR_TrackFX_FormatParamValueNormalized(track, fx, param, value, buf, buf_sz)
    
    Note: only works with FX that support Cockos VST extensions.
    """
    a=_ft['TrackFX_FormatParamValueNormalized']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),c_double(value),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return (r,track,fx,param,value,rpr_unpacks(t[4]),buf_sz)
     
def RPR_TrackFX_GetByName(track,fxname,instantiate):
    """
    Python: Int  RPR_TrackFX_GetByName(MediaTrack track, String fxname, Boolean instantiate)
    
    Get the index of the first track FX insert that matches fxname. If the FX is not in the chain and instantiate is true, it will be inserted. See TrackFX_GetInstrument
    , TrackFX_GetEQ
    . Deprecated in favor of TrackFX_AddByName.
    """
    a=_ft['TrackFX_GetByName']
    f=CFUNCTYPE(c_int,c_uint64,c_char_p,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),rpr_packsc(fxname),c_byte(instantiate))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TrackFX_GetChainVisible(track):
    """
    Python: Int  RPR_TrackFX_GetChainVisible(MediaTrack track)
    
    returns index of effect visible in chain, or -1 for chain hidden, or -2 for chain visible but no effect selected
    """
    a=_ft['TrackFX_GetChainVisible']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_TrackFX_GetCount(track):
    """
    Python: Int  RPR_TrackFX_GetCount(MediaTrack track)
    """
    a=_ft['TrackFX_GetCount']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_TrackFX_GetEnabled(track,fx):
    """
    Python: Boolean  RPR_TrackFX_GetEnabled(MediaTrack track, Int fx)
    
    See TrackFX_SetEnabled
    """
    a=_ft['TrackFX_GetEnabled']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TrackFX_GetEQ(track,instantiate):
    """
    Python: Int  RPR_TrackFX_GetEQ(MediaTrack track, Boolean instantiate)
    
    Get the index of ReaEQ in the track FX chain. If ReaEQ is not in the chain and instantiate is true, it will be inserted. See TrackFX_GetInstrument
    , TrackFX_GetByName
    .
    """
    a=_ft['TrackFX_GetEQ']
    f=CFUNCTYPE(c_int,c_uint64,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_byte(instantiate))
    r=f(t[0],t[1])
    return r
     
def RPR_TrackFX_GetEQBandEnabled(track,fxidx,bandtype,bandidx):
    """
    Python: Boolean  RPR_TrackFX_GetEQBandEnabled(MediaTrack track, Int fxidx, Int bandtype, Int bandidx)
    
    Returns true if the EQ band is enabled.
    
    Returns false if the band is disabled, or if track/fxidx is not ReaEQ.
    
    Bandtype: 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
    
    Bandidx: 0=first band matching bandtype, 1=2nd band matching bandtype, etc.
    
    See TrackFX_GetEQ
    , TrackFX_GetEQParam
    , TrackFX_SetEQParam
    , TrackFX_SetEQBandEnabled
    .
    """
    a=_ft['TrackFX_GetEQBandEnabled']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fxidx),c_int(bandtype),c_int(bandidx))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TrackFX_GetEQParam(track,fxidx,paramidx,bandtypeOut,bandidxOut,paramtypeOut,normvalOut):
    """
    Python: (Boolean retval, MediaTrack track, Int fxidx, Int paramidx, Int bandtypeOut, Int bandidxOut, Int paramtypeOut, Float normvalOut) = RPR_TrackFX_GetEQParam(track, fxidx, paramidx, bandtypeOut, bandidxOut, paramtypeOut, normvalOut)
    
    Returns false if track/fxidx is not ReaEQ.
    
    Bandtype: -1=master gain, 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
    
    Bandidx (ignored for master gain): 0=first band matching bandtype, 1=2nd band matching bandtype, etc.
    
    Paramtype (ignored for master gain): 0=freq, 1=gain, 2=Q.
    
    See TrackFX_GetEQ
    , TrackFX_SetEQParam
    , TrackFX_GetEQBandEnabled
    , TrackFX_SetEQBandEnabled
    .
    """
    a=_ft['TrackFX_GetEQParam']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fxidx),c_int(paramidx),c_int(bandtypeOut),c_int(bandidxOut),c_int(paramtypeOut),c_double(normvalOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]))
    return (r,track,fxidx,paramidx,int(t[3].value),int(t[4].value),int(t[5].value),float(t[6].value))
     
def RPR_TrackFX_GetFloatingWindow(track,index):
    """
    Python: HWND  RPR_TrackFX_GetFloatingWindow(MediaTrack track, Int index)
    
    returns HWND of floating window for effect index, if any
    """
    a=_ft['TrackFX_GetFloatingWindow']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(index))
    r=f(t[0],t[1])
    return rpr_unpackp('HWND',r)
     
def RPR_TrackFX_GetFormattedParamValue(track,fx,param,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, Int param, String buf, Int buf_sz) = RPR_TrackFX_GetFormattedParamValue(track, fx, param, buf, buf_sz)
    """
    a=_ft['TrackFX_GetFormattedParamValue']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,track,fx,param,rpr_unpacks(t[3]),buf_sz)
     
def RPR_TrackFX_GetFXGUID(track,fx):
    """
    Python: GUID  RPR_TrackFX_GetFXGUID(MediaTrack track, Int fx)
    """
    a=_ft['TrackFX_GetFXGUID']
    f=CFUNCTYPE(c_uint64,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx))
    r=f(t[0],t[1])
    return rpr_unpackp('GUID*',r)
     
def RPR_TrackFX_GetFXName(track,fx,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, String buf, Int buf_sz) = RPR_TrackFX_GetFXName(track, fx, buf, buf_sz)
    """
    a=_ft['TrackFX_GetFXName']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,fx,rpr_unpacks(t[2]),buf_sz)
     
def RPR_TrackFX_GetInstrument(track):
    """
    Python: Int  RPR_TrackFX_GetInstrument(MediaTrack track)
    
    Get the index of the first track FX insert that is a virtual instrument, or -1 if none. See TrackFX_GetEQ
    , TrackFX_GetByName
    .
    """
    a=_ft['TrackFX_GetInstrument']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_TrackFX_GetIOSize(track,fx,inputPinsOutOptional,outputPinsOutOptional):
    """
    Python: (Int retval, MediaTrack track, Int fx, Int inputPinsOutOptional, Int outputPinsOutOptional) = RPR_TrackFX_GetIOSize(track, fx, inputPinsOutOptional, outputPinsOutOptional)
    
    sets the number of input/output pins for FX if available, returns plug-in type or -1 on error
    """
    a=_ft['TrackFX_GetIOSize']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(inputPinsOutOptional),c_int(outputPinsOutOptional))
    r=f(t[0],t[1],byref(t[2]),byref(t[3]))
    return (r,track,fx,int(t[2].value),int(t[3].value))
     
def RPR_TrackFX_GetNamedConfigParm(track,fx,parmname,bufOut,bufOut_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, String parmname, String bufOut, Int bufOut_sz) = RPR_TrackFX_GetNamedConfigParm(track, fx, parmname, bufOut, bufOut_sz)
    
    gets plug-in specific named configuration value (returns true on success). Special values: 'pdc' returns PDC latency. 'in_pin_0' returns name of first input pin (if available), 'out_pin_0' returns name of first output pin (if available), etc.
    """
    a=_ft['TrackFX_GetNamedConfigParm']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),rpr_packsc(parmname),rpr_packs(bufOut),c_int(bufOut_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,track,fx,parmname,rpr_unpacks(t[3]),bufOut_sz)
     
def RPR_TrackFX_GetNumParams(track,fx):
    """
    Python: Int  RPR_TrackFX_GetNumParams(MediaTrack track, Int fx)
    """
    a=_ft['TrackFX_GetNumParams']
    f=CFUNCTYPE(c_int,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TrackFX_GetOffline(track,fx):
    """
    Python: Boolean  RPR_TrackFX_GetOffline(MediaTrack track, Int fx)
    
    See TrackFX_SetOffline
    """
    a=_ft['TrackFX_GetOffline']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TrackFX_GetOpen(track,fx):
    """
    Python: Boolean  RPR_TrackFX_GetOpen(MediaTrack track, Int fx)
    
    Returns true if this FX UI is open in the FX chain window or a floating window. See TrackFX_SetOpen
    """
    a=_ft['TrackFX_GetOpen']
    f=CFUNCTYPE(c_byte,c_uint64,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx))
    r=f(t[0],t[1])
    return r
     
def RPR_TrackFX_GetParam(track,fx,param,minvalOut,maxvalOut):
    """
    Python: (Float retval, MediaTrack track, Int fx, Int param, Float minvalOut, Float maxvalOut) = RPR_TrackFX_GetParam(track, fx, param, minvalOut, maxvalOut)
    """
    a=_ft['TrackFX_GetParam']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),c_double(minvalOut),c_double(maxvalOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]))
    return (r,track,fx,param,float(t[3].value),float(t[4].value))
     
def RPR_TrackFX_GetParameterStepSizes(track,fx,param,stepOut,smallstepOut,largestepOut,istoggleOut):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, Int param, Float stepOut, Float smallstepOut, Float largestepOut, Boolean istoggleOut) = RPR_TrackFX_GetParameterStepSizes(track, fx, param, stepOut, smallstepOut, largestepOut, istoggleOut)
    """
    a=_ft['TrackFX_GetParameterStepSizes']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_void_p,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),c_double(stepOut),c_double(smallstepOut),c_double(largestepOut),c_byte(istoggleOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),byref(t[5]),byref(t[6]))
    return (r,track,fx,param,float(t[3].value),float(t[4].value),float(t[5].value),int(t[6].value))
     
def RPR_TrackFX_GetParamEx(track,fx,param,minvalOut,maxvalOut,midvalOut):
    """
    Python: (Float retval, MediaTrack track, Int fx, Int param, Float minvalOut, Float maxvalOut, Float midvalOut) = RPR_TrackFX_GetParamEx(track, fx, param, minvalOut, maxvalOut, midvalOut)
    """
    a=_ft['TrackFX_GetParamEx']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int,c_void_p,c_void_p,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),c_double(minvalOut),c_double(maxvalOut),c_double(midvalOut))
    r=f(t[0],t[1],t[2],byref(t[3]),byref(t[4]),byref(t[5]))
    return (r,track,fx,param,float(t[3].value),float(t[4].value),float(t[5].value))
     
def RPR_TrackFX_GetParamName(track,fx,param,buf,buf_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, Int param, String buf, Int buf_sz) = RPR_TrackFX_GetParamName(track, fx, param, buf, buf_sz)
    """
    a=_ft['TrackFX_GetParamName']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),rpr_packs(buf),c_int(buf_sz))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return (r,track,fx,param,rpr_unpacks(t[3]),buf_sz)
     
def RPR_TrackFX_GetParamNormalized(track,fx,param):
    """
    Python: Float  RPR_TrackFX_GetParamNormalized(MediaTrack track, Int fx, Int param)
    """
    a=_ft['TrackFX_GetParamNormalized']
    f=CFUNCTYPE(c_double,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TrackFX_GetPinMappings(tr,fx,isoutput,pin,high32OutOptional):
    """
    Python: (Int retval, MediaTrack tr, Int fx, Int isoutput, Int pin, Int high32OutOptional) = RPR_TrackFX_GetPinMappings(tr, fx, isoutput, pin, high32OutOptional)
    
    gets the effective channel mapping bitmask for a particular pin. high32OutOptional will be set to the high 32 bits
    """
    a=_ft['TrackFX_GetPinMappings']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_int,c_int,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(fx),c_int(isoutput),c_int(pin),c_int(high32OutOptional))
    r=f(t[0],t[1],t[2],t[3],byref(t[4]))
    return (r,tr,fx,isoutput,pin,int(t[4].value))
     
def RPR_TrackFX_GetPreset(track,fx,presetname,presetname_sz):
    """
    Python: (Boolean retval, MediaTrack track, Int fx, String presetname, Int presetname_sz) = RPR_TrackFX_GetPreset(track, fx, presetname, presetname_sz)
    
    Get the name of the preset currently showing in the REAPER dropdown, or the full path to a factory preset file for VST3 plug-ins (.vstpreset). Returns false if the current FX parameters do not exactly match the preset (in other words, if the user loaded the preset but moved the knobs afterward). See TrackFX_SetPreset
    .
    """
    a=_ft['TrackFX_GetPreset']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),rpr_packs(presetname),c_int(presetname_sz))
    r=f(t[0],t[1],t[2],t[3])
    return (r,track,fx,rpr_unpacks(t[2]),presetname_sz)
     
def RPR_TrackFX_GetPresetIndex(track,fx,numberOfPresetsOut):
    """
    Python: (Int retval, MediaTrack track, Int fx, Int numberOfPresetsOut) = RPR_TrackFX_GetPresetIndex(track, fx, numberOfPresetsOut)
    
    Returns current preset index, or -1 if error. numberOfPresetsOut will be set to total number of presets available. See TrackFX_SetPresetByIndex
    """
    a=_ft['TrackFX_GetPresetIndex']
    f=CFUNCTYPE(c_int,c_uint64,c_int,c_void_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(numberOfPresetsOut))
    r=f(t[0],t[1],byref(t[2]))
    return (r,track,fx,int(t[2].value))
     
def RPR_TrackFX_GetRecChainVisible(track):
    """
    Python: Int  RPR_TrackFX_GetRecChainVisible(MediaTrack track)
    
    returns index of effect visible in record input chain, or -1 for chain hidden, or -2 for chain visible but no effect selected
    """
    a=_ft['TrackFX_GetRecChainVisible']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_TrackFX_GetRecCount(track):
    """
    Python: Int  RPR_TrackFX_GetRecCount(MediaTrack track)
    
    returns count of record input FX. To access record input FX, use a FX indices [0x1000000..0x1000000+n). On the master track, this accesses monitoring FX rather than record input FX.
    """
    a=_ft['TrackFX_GetRecCount']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('MediaTrack*',track),)
    r=f(t[0])
    return r
     
def RPR_TrackFX_GetUserPresetFilename(track,fx,fn,fn_sz):
    """
    Python: (MediaTrack track, Int fx, String fn, Int fn_sz) = RPR_TrackFX_GetUserPresetFilename(track, fx, fn, fn_sz)
    """
    a=_ft['TrackFX_GetUserPresetFilename']
    f=CFUNCTYPE(None,c_uint64,c_int,c_char_p,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),rpr_packs(fn),c_int(fn_sz))
    f(t[0],t[1],t[2],t[3])
    return (track,fx,rpr_unpacks(t[2]),fn_sz)
     
def RPR_TrackFX_NavigatePresets(track,fx,presetmove):
    """
    Python: Boolean  RPR_TrackFX_NavigatePresets(MediaTrack track, Int fx, Int presetmove)
    
    presetmove==1 activates the next preset, presetmove==-1 activates the previous preset, etc.
    """
    a=_ft['TrackFX_NavigatePresets']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(presetmove))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TrackFX_SetEnabled(track,fx,enabled):
    """
    Python: RPR_TrackFX_SetEnabled(MediaTrack track, Int fx, Boolean enabled)
    
    See TrackFX_GetEnabled
    """
    a=_ft['TrackFX_SetEnabled']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_byte(enabled))
    f(t[0],t[1],t[2])
     
def RPR_TrackFX_SetEQBandEnabled(track,fxidx,bandtype,bandidx,enable):
    """
    Python: Boolean  RPR_TrackFX_SetEQBandEnabled(MediaTrack track, Int fxidx, Int bandtype, Int bandidx, Boolean enable)
    
    Enable or disable a ReaEQ band.
    
    Returns false if track/fxidx is not ReaEQ.
    
    Bandtype: 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
    
    Bandidx: 0=first band matching bandtype, 1=2nd band matching bandtype, etc.
    
    See TrackFX_GetEQ
    , TrackFX_GetEQParam
    , TrackFX_SetEQParam
    , TrackFX_GetEQBandEnabled
    .
    """
    a=_ft['TrackFX_SetEQBandEnabled']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fxidx),c_int(bandtype),c_int(bandidx),c_byte(enable))
    r=f(t[0],t[1],t[2],t[3],t[4])
    return r
     
def RPR_TrackFX_SetEQParam(track,fxidx,bandtype,bandidx,paramtype,val,isnorm):
    """
    Python: Boolean  RPR_TrackFX_SetEQParam(MediaTrack track, Int fxidx, Int bandtype, Int bandidx, Int paramtype, Float val, Boolean isnorm)
    
    Returns false if track/fxidx is not ReaEQ. Targets a band matching bandtype.
    
    Bandtype: -1=master gain, 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
    
    Bandidx (ignored for master gain): 0=target first band matching bandtype, 1=target 2nd band matching bandtype, etc.
    
    Paramtype (ignored for master gain): 0=freq, 1=gain, 2=Q.
    
    See TrackFX_GetEQ
    , TrackFX_GetEQParam
    , TrackFX_GetEQBandEnabled
    , TrackFX_SetEQBandEnabled
    .
    """
    a=_ft['TrackFX_SetEQParam']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_int,c_int,c_double,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fxidx),c_int(bandtype),c_int(bandidx),c_int(paramtype),c_double(val),c_byte(isnorm))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5],t[6])
    return r
     
def RPR_TrackFX_SetNamedConfigParm(track,fx,parmname,value):
    """
    Python: Boolean  RPR_TrackFX_SetNamedConfigParm(MediaTrack track, Int fx, String parmname, String value)
    
    sets plug-in specific named configuration value (returns true on success)
    """
    a=_ft['TrackFX_SetNamedConfigParm']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),rpr_packsc(parmname),rpr_packsc(value))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TrackFX_SetOffline(track,fx,offline):
    """
    Python: RPR_TrackFX_SetOffline(MediaTrack track, Int fx, Boolean offline)
    
    See TrackFX_GetOffline
    """
    a=_ft['TrackFX_SetOffline']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_byte(offline))
    f(t[0],t[1],t[2])
     
def RPR_TrackFX_SetOpen(track,fx,Open):
    """
    Python: RPR_TrackFX_SetOpen(MediaTrack track, Int fx, Boolean open)
    
    Open this FX UI. See TrackFX_GetOpen
    """
    a=_ft['TrackFX_SetOpen']
    f=CFUNCTYPE(None,c_uint64,c_int,c_byte)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_byte(Open))
    f(t[0],t[1],t[2])
     
def RPR_TrackFX_SetParam(track,fx,param,val):
    """
    Python: Boolean  RPR_TrackFX_SetParam(MediaTrack track, Int fx, Int param, Float val)
    """
    a=_ft['TrackFX_SetParam']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),c_double(val))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TrackFX_SetParamNormalized(track,fx,param,value):
    """
    Python: Boolean  RPR_TrackFX_SetParamNormalized(MediaTrack track, Int fx, Int param, Float value)
    """
    a=_ft['TrackFX_SetParamNormalized']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_double)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(param),c_double(value))
    r=f(t[0],t[1],t[2],t[3])
    return r
     
def RPR_TrackFX_SetPinMappings(tr,fx,isoutput,pin,low32bits,hi32bits):
    """
    Python: Boolean  RPR_TrackFX_SetPinMappings(MediaTrack tr, Int fx, Int isoutput, Int pin, Int low32bits, Int hi32bits)
    
    sets the channel mapping bitmask for a particular pin. returns false if unsupported (not all types of plug-ins support this capability)
    """
    a=_ft['TrackFX_SetPinMappings']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int,c_int,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',tr),c_int(fx),c_int(isoutput),c_int(pin),c_int(low32bits),c_int(hi32bits))
    r=f(t[0],t[1],t[2],t[3],t[4],t[5])
    return r
     
def RPR_TrackFX_SetPreset(track,fx,presetname):
    """
    Python: Boolean  RPR_TrackFX_SetPreset(MediaTrack track, Int fx, String presetname)
    
    Activate a preset with the name shown in the REAPER dropdown. Full paths to .vstpreset files are also supported for VST3 plug-ins. See TrackFX_GetPreset
    .
    """
    a=_ft['TrackFX_SetPreset']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_char_p)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),rpr_packsc(presetname))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TrackFX_SetPresetByIndex(track,fx,idx):
    """
    Python: Boolean  RPR_TrackFX_SetPresetByIndex(MediaTrack track, Int fx, Int idx)
    
    Sets the preset idx, or the factory preset (idx==-2), or the default user preset (idx==-1). Returns true on success. See TrackFX_GetPresetIndex
    .
    """
    a=_ft['TrackFX_SetPresetByIndex']
    f=CFUNCTYPE(c_byte,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(fx),c_int(idx))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_TrackFX_Show(track,index,showFlag):
    """
    Python: RPR_TrackFX_Show(MediaTrack track, Int index, Int showFlag)
    
    showflag=0 for hidechain, =1 for show chain(index valid), =2 for hide floating window(index valid), =3 for show floating window (index valid)
    """
    a=_ft['TrackFX_Show']
    f=CFUNCTYPE(None,c_uint64,c_int,c_int)(a)
    t=(rpr_packp('MediaTrack*',track),c_int(index),c_int(showFlag))
    f(t[0],t[1],t[2])
     
def RPR_TrackList_AdjustWindows(isMinor):
    """
    Python: RPR_TrackList_AdjustWindows(Boolean isMinor)
    """
    a=_ft['TrackList_AdjustWindows']
    f=CFUNCTYPE(None,c_byte)(a)
    t=(c_byte(isMinor),)
    f(t[0])
     
def RPR_TrackList_UpdateAllExternalSurfaces():
    """
    Python: RPR_TrackList_UpdateAllExternalSurfaces()
    """
    a=_ft['TrackList_UpdateAllExternalSurfaces']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_Undo_BeginBlock():
    """
    Python: RPR_Undo_BeginBlock()
    
    call to start a new block
    """
    a=_ft['Undo_BeginBlock']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_Undo_BeginBlock2(proj):
    """
    Python: RPR_Undo_BeginBlock2(ReaProject proj)
    
    call to start a new block
    """
    a=_ft['Undo_BeginBlock2']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    f(t[0])
     
def RPR_Undo_CanRedo2(proj):
    """
    Python: String  RPR_Undo_CanRedo2(ReaProject proj)
    
    returns string of next action,if able,NULL if not
    """
    a=_ft['Undo_CanRedo2']
    f=CFUNCTYPE(c_char_p,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_Undo_CanUndo2(proj):
    """
    Python: String  RPR_Undo_CanUndo2(ReaProject proj)
    
    returns string of last action,if able,NULL if not
    """
    a=_ft['Undo_CanUndo2']
    f=CFUNCTYPE(c_char_p,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return str(r.decode())
     
def RPR_Undo_DoRedo2(proj):
    """
    Python: Int  RPR_Undo_DoRedo2(ReaProject proj)
    
    nonzero if success
    """
    a=_ft['Undo_DoRedo2']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_Undo_DoUndo2(proj):
    """
    Python: Int  RPR_Undo_DoUndo2(ReaProject proj)
    
    nonzero if success
    """
    a=_ft['Undo_DoUndo2']
    f=CFUNCTYPE(c_int,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),)
    r=f(t[0])
    return r
     
def RPR_Undo_EndBlock(descchange,extraflags):
    """
    Python: RPR_Undo_EndBlock(String descchange, Int extraflags)
    
    call to end the block,with extra flags if any,and a description
    """
    a=_ft['Undo_EndBlock']
    f=CFUNCTYPE(None,c_char_p,c_int)(a)
    t=(rpr_packsc(descchange),c_int(extraflags))
    f(t[0],t[1])
     
def RPR_Undo_EndBlock2(proj,descchange,extraflags):
    """
    Python: RPR_Undo_EndBlock2(ReaProject proj, String descchange, Int extraflags)
    
    call to end the block,with extra flags if any,and a description
    """
    a=_ft['Undo_EndBlock2']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(descchange),c_int(extraflags))
    f(t[0],t[1],t[2])
     
def RPR_Undo_OnStateChange(descchange):
    """
    Python: RPR_Undo_OnStateChange(String descchange)
    
    limited state change to items
    """
    a=_ft['Undo_OnStateChange']
    f=CFUNCTYPE(None,c_char_p)(a)
    t=(rpr_packsc(descchange),)
    f(t[0])
     
def RPR_Undo_OnStateChange2(proj,descchange):
    """
    Python: RPR_Undo_OnStateChange2(ReaProject proj, String descchange)
    
    limited state change to items
    """
    a=_ft['Undo_OnStateChange2']
    f=CFUNCTYPE(None,c_uint64,c_char_p)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(descchange))
    f(t[0],t[1])
     
def RPR_Undo_OnStateChange_Item(proj,name,item):
    """
    Python: RPR_Undo_OnStateChange_Item(ReaProject proj, String name, MediaItem item)
    """
    a=_ft['Undo_OnStateChange_Item']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_uint64)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(name),rpr_packp('MediaItem*',item))
    f(t[0],t[1],t[2])
     
def RPR_Undo_OnStateChangeEx(descchange,whichStates,trackparm):
    """
    Python: RPR_Undo_OnStateChangeEx(String descchange, Int whichStates, Int trackparm)
    
    trackparm=-1 by default,or if updating one fx chain,you can specify track index
    """
    a=_ft['Undo_OnStateChangeEx']
    f=CFUNCTYPE(None,c_char_p,c_int,c_int)(a)
    t=(rpr_packsc(descchange),c_int(whichStates),c_int(trackparm))
    f(t[0],t[1],t[2])
     
def RPR_Undo_OnStateChangeEx2(proj,descchange,whichStates,trackparm):
    """
    Python: RPR_Undo_OnStateChangeEx2(ReaProject proj, String descchange, Int whichStates, Int trackparm)
    
    trackparm=-1 by default,or if updating one fx chain,you can specify track index
    """
    a=_ft['Undo_OnStateChangeEx2']
    f=CFUNCTYPE(None,c_uint64,c_char_p,c_int,c_int)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packsc(descchange),c_int(whichStates),c_int(trackparm))
    f(t[0],t[1],t[2],t[3])
     
def RPR_UpdateArrange():
    """
    Python: RPR_UpdateArrange()
    
    Redraw the arrange view
    """
    a=_ft['UpdateArrange']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_UpdateItemInProject(item):
    """
    Python: RPR_UpdateItemInProject(MediaItem item)
    """
    a=_ft['UpdateItemInProject']
    f=CFUNCTYPE(None,c_uint64)(a)
    t=(rpr_packp('MediaItem*',item),)
    f(t[0])
     
def RPR_UpdateTimeline():
    """
    Python: RPR_UpdateTimeline()
    
    Redraw the arrange view and ruler
    """
    a=_ft['UpdateTimeline']
    f=CFUNCTYPE(None)(a)
    f()
     
def RPR_ValidatePtr2(proj,pointer,ctypename):
    """
    Python: Boolean  RPR_ValidatePtr2(ReaProject proj, void pointer, String ctypename)
    
    Return true if the pointer is a valid object of the right type in proj (proj is ignored if pointer is itself a project). Supported types are: ReaProject*, MediaTrack*, MediaItem*, MediaItem_Take*, TrackEnvelope* and PCM_source*.
    """
    a=_ft['ValidatePtr2']
    f=CFUNCTYPE(c_byte,c_uint64,c_uint64,c_char_p)(a)
    t=(rpr_packp('ReaProject*',proj),rpr_packp('void*',pointer),rpr_packsc(ctypename))
    r=f(t[0],t[1],t[2])
    return r
     
def RPR_ViewPrefs(page,pageByName):
    """
    Python: RPR_ViewPrefs(Int page, String pageByName)
    
    Opens the prefs to a page, use pageByName if page is 0.
    """
    a=_ft['ViewPrefs']
    f=CFUNCTYPE(None,c_int,c_char_p)(a)
    t=(c_int(page),rpr_packsc(pageByName))
    f(t[0],t[1])
     
