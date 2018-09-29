-- REAPER 5.95, SWS 2.9.7


local original_reaper = reaper
local reaper = {}


---Lua: MediaItem reaper.AddMediaItemToTrack(MediaTrack tr)
---
---
---creates a new media item.
function reaper.AddMediaItemToTrack(tr)
end


---Lua: integer reaper.AddProjectMarker(ReaProject proj, boolean isrgn, number pos, number rgnend, string name, integer wantidx)
---
---
---Returns the index of the created marker/region, or -1 on failure. Supply wantidx>=0 if you want a particular index number, but you'll get a different index number a region and wantidx is already in use.
function reaper.AddProjectMarker(proj, isrgn, pos, rgnend, name, wantidx)
end


---Lua: integer reaper.AddProjectMarker2(ReaProject proj, boolean isrgn, number pos, number rgnend, string name, integer wantidx, integer color)
---
---
---Returns the index of the created marker/region, or -1 on failure. Supply wantidx>=0 if you want a particular index number, but you'll get a different index number a region and wantidx is already in use. color should be 0 (default color), or ColorToNative(r,g,b)|0x1000000
function reaper.AddProjectMarker2(proj, isrgn, pos, rgnend, name, wantidx, color)
end


---Lua: integer reaper.AddRemoveReaScript(boolean add, integer sectionID, string scriptfn, boolean commit)
---
---
---Add a ReaScript (return the new command ID, or 0 if failed) or remove a ReaScript (return >0 on success). Use commit==true when adding/removing a single script. When bulk adding/removing n scripts, you can optimize the n-1 first calls with commit==false and commit==true for the last call.
function reaper.AddRemoveReaScript(add, sectionID, scriptfn, commit)
end


---Lua: MediaItem_Take reaper.AddTakeToMediaItem(MediaItem item)
---
---
---creates a new take in an item
function reaper.AddTakeToMediaItem(item)
end


---Lua: boolean reaper.AddTempoTimeSigMarker(ReaProject proj, number timepos, number bpm, integer timesig_num, integer timesig_denom, boolean lineartempochange)
---
---
---Deprecated. Use SetTempoTimeSigMarker with ptidx=-1.
function reaper.AddTempoTimeSigMarker(proj, timepos, bpm, timesig_num, timesig_denom, lineartempochange)
end


---Lua: reaper.adjustZoom(number amt, integer forceset, boolean doupd, integer centermode)
---
---
---forceset=0,doupd=true,centermode=-1 for default
function reaper.adjustZoom(amt, forceset, doupd, centermode)
end


---Lua: boolean reaper.AnyTrackSolo(ReaProject proj)
function reaper.AnyTrackSolo(proj)
end


---Lua: boolean reaper.APIExists(string function_name)
---
---
---Returns true if function_name exists in the REAPER API
function reaper.APIExists(function_name)
end


---Lua: reaper.APITest()
---
---
---Displays a message window if the API was successfully called.
function reaper.APITest()
end


---Lua: boolean reaper.ApplyNudge(ReaProject project, integer nudgeflag, integer nudgewhat, integer nudgeunits, number value, boolean reverse, integer copies)
---
---
---nudgeflag: &1=set to value (otherwise nudge by value), &2=snap
---
---nudgewhat: 0=position, 1=left trim, 2=left edge, 3=right edge, 4=contents, 5=duplicate, 6=edit cursor
---
---nudgeunit: 0=ms, 1=seconds, 2=grid, 3=256th notes, ..., 15=whole notes, 16=measures.beats (1.15 = 1 measure + 1.5 beats), 17=samples, 18=frames, 19=pixels, 20=item lengths, 21=item selections
---
---value: amount to nudge by, or value to set to
---
---reverse: in nudge mode, nudges left (otherwise ignored)
---
---copies: in nudge duplicate mode, number of copies (otherwise ignored)
function reaper.ApplyNudge(project, nudgeflag, nudgewhat, nudgeunits, value, reverse, copies)
end


---Lua: reaper.ArmCommand(integer cmd, string sectionname)
---
---
---arms a command (or disarms if 0 passed) in section sectionname (empty string for main)
function reaper.ArmCommand(cmd, sectionname)
end


---Lua: reaper.Audio_Init()
---
---
---open all audio and MIDI devices, if not open
function reaper.Audio_Init()
end


---Lua: integer reaper.Audio_IsPreBuffer()
---
---
---is in pre-buffer? threadsafe
function reaper.Audio_IsPreBuffer()
end


---Lua: integer reaper.Audio_IsRunning()
---
---
---is audio running at all? threadsafe
function reaper.Audio_IsRunning()
end


---Lua: reaper.Audio_Quit()
---
---
---close all audio and MIDI devices, if open
function reaper.Audio_Quit()
end


---Lua: boolean reaper.AudioAccessorValidateState(AudioAccessor accessor)
---
---
---Validates the current state of the audio accessor -- must ONLY call this from the main thread. Returns true if the state changed.
function reaper.AudioAccessorValidateState(accessor)
end


---Lua: reaper.BypassFxAllTracks(integer bypass)
---
---
----1 = bypass all if not all bypassed,otherwise unbypass all
function reaper.BypassFxAllTracks(bypass)
end


---Lua: reaper.ClearAllRecArmed()
function reaper.ClearAllRecArmed()
end


---Lua: reaper.ClearConsole()
---
---
---Clear the ReaScript console. See ShowConsoleMsg
function reaper.ClearConsole()
end


---Lua: reaper.ClearPeakCache()
---
---
---resets the global peak caches
function reaper.ClearPeakCache()
end


---Lua: number r, number g, number b = reaper.ColorFromNative(integer col)
---
---
---Extract RGB values from an OS dependent color. See ColorToNative
---.
function reaper.ColorFromNative(col)
end


---Lua: integer reaper.ColorToNative(integer r, integer g, integer b)
---
---
---Make an OS dependent color from RGB values (e.g. RGB() macro on Windows). r,g and b are in [0..255]. See ColorFromNative
---.
function reaper.ColorToNative(r, g, b)
end


---Lua: integer reaper.CountAutomationItems(TrackEnvelope env)
---
---
---Returns the number of automation items on this envelope. See GetSetAutomationItemInfo
function reaper.CountAutomationItems(env)
end


---Lua: integer reaper.CountEnvelopePoints(TrackEnvelope envelope)
---
---
---Returns the number of points in the envelope.
function reaper.CountEnvelopePoints(envelope)
end


---Lua: integer reaper.CountEnvelopePointsEx(TrackEnvelope envelope, integer autoitem_idx)
---
---
---Returns the number of points in the envelope. autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc.
function reaper.CountEnvelopePointsEx(envelope, autoitem_idx)
end


---Lua: integer reaper.CountMediaItems(ReaProject proj)
---
---
---count the number of items in the project (proj=0 for active project)
function reaper.CountMediaItems(proj)
end


---Lua: integer retval, number num_markers, number num_regions = reaper.CountProjectMarkers(ReaProject proj)
---
---
---num_markersOut and num_regionsOut may be NULL.
function reaper.CountProjectMarkers(proj)
end


---Lua: integer reaper.CountSelectedMediaItems(ReaProject proj)
---
---
---count the number of selected items in the project (proj=0 for active project)
function reaper.CountSelectedMediaItems(proj)
end


---Lua: integer reaper.CountSelectedTracks(ReaProject proj)
---
---
---Count the number of selected tracks in the project (proj=0 for active project). This function ignores the master track, see CountSelectedTracks2
---.
function reaper.CountSelectedTracks(proj)
end


---Lua: integer reaper.CountSelectedTracks2(ReaProject proj, boolean wantmaster)
---
---
---Count the number of selected tracks in the project (proj=0 for active project).
function reaper.CountSelectedTracks2(proj, wantmaster)
end


---Lua: integer reaper.CountTakeEnvelopes(MediaItem_Take take)
---
---
---See GetTakeEnvelope
function reaper.CountTakeEnvelopes(take)
end


---Lua: integer reaper.CountTakes(MediaItem item)
---
---
---count the number of takes in the item
function reaper.CountTakes(item)
end


---Lua: integer reaper.CountTCPFXParms(ReaProject project, MediaTrack track)
---
---
---Count the number of FX parameter knobs displayed on the track control panel.
function reaper.CountTCPFXParms(project, track)
end


---Lua: integer reaper.CountTempoTimeSigMarkers(ReaProject proj)
---
---
---Count the number of tempo/time signature markers in the project. See GetTempoTimeSigMarker
---, SetTempoTimeSigMarker
---, AddTempoTimeSigMarker
---.
function reaper.CountTempoTimeSigMarkers(proj)
end


---Lua: integer reaper.CountTrackEnvelopes(MediaTrack track)
---
---
---see GetTrackEnvelope
function reaper.CountTrackEnvelopes(track)
end


---Lua: integer reaper.CountTrackMediaItems(MediaTrack track)
---
---
---count the number of items in the track
function reaper.CountTrackMediaItems(track)
end


---Lua: integer reaper.CountTracks(ReaProject proj)
---
---
---count the number of tracks in the project (proj=0 for active project)
function reaper.CountTracks(proj)
end


---Lua: MediaItem reaper.CreateNewMIDIItemInProj(MediaTrack track, number starttime, number endtime, optional boolean qnIn)
---
---
---Create a new MIDI media item, containing no MIDI events. Time is in seconds unless qn is set.
function reaper.CreateNewMIDIItemInProj(track, starttime, endtime, qnIn)
end


---Lua: AudioAccessor reaper.CreateTakeAudioAccessor(MediaItem_Take take)
---
---
---Create an audio accessor object for this take. Must only call from the main thread. See CreateTrackAudioAccessor
---, DestroyAudioAccessor
---, GetAudioAccessorHash
---, GetAudioAccessorStartTime
---, GetAudioAccessorEndTime
---, GetAudioAccessorSamples
---.
function reaper.CreateTakeAudioAccessor(take)
end


---Lua: AudioAccessor reaper.CreateTrackAudioAccessor(MediaTrack track)
---
---
---Create an audio accessor object for this track. Must only call from the main thread. See CreateTakeAudioAccessor
---, DestroyAudioAccessor
---, GetAudioAccessorHash
---, GetAudioAccessorStartTime
---, GetAudioAccessorEndTime
---, GetAudioAccessorSamples
---.
function reaper.CreateTrackAudioAccessor(track)
end


---Lua: integer reaper.CreateTrackSend(MediaTrack tr, MediaTrack desttrIn)
---
---
---Create a send/receive (desttrInOptional!=NULL), or a hardware output (desttrInOptional==NULL) with default properties, return >=0 on success (== new send/receive index). See RemoveTrackSend
---, GetSetTrackSendInfo
---, GetTrackSendInfo_Value
---, SetTrackSendInfo_Value
---.
function reaper.CreateTrackSend(tr, desttrIn)
end


---Lua: reaper.CSurf_FlushUndo(boolean force)
---
---
---call this to force flushing of the undo states after using CSurf_On*Change()
function reaper.CSurf_FlushUndo(force)
end


---Lua: boolean reaper.CSurf_GetTouchState(MediaTrack trackid, integer isPan)
function reaper.CSurf_GetTouchState(trackid, isPan)
end


---Lua: reaper.CSurf_GoEnd()
function reaper.CSurf_GoEnd()
end


---Lua: reaper.CSurf_GoStart()
function reaper.CSurf_GoStart()
end


---Lua: integer reaper.CSurf_NumTracks(boolean mcpView)
function reaper.CSurf_NumTracks(mcpView)
end


---Lua: reaper.CSurf_OnArrow(integer whichdir, boolean wantzoom)
function reaper.CSurf_OnArrow(whichdir, wantzoom)
end


---Lua: reaper.CSurf_OnFwd(integer seekplay)
function reaper.CSurf_OnFwd(seekplay)
end


---Lua: boolean reaper.CSurf_OnFXChange(MediaTrack trackid, integer en)
function reaper.CSurf_OnFXChange(trackid, en)
end


---Lua: integer reaper.CSurf_OnInputMonitorChange(MediaTrack trackid, integer monitor)
function reaper.CSurf_OnInputMonitorChange(trackid, monitor)
end


---Lua: integer reaper.CSurf_OnInputMonitorChangeEx(MediaTrack trackid, integer monitor, boolean allowgang)
function reaper.CSurf_OnInputMonitorChangeEx(trackid, monitor, allowgang)
end


---Lua: boolean reaper.CSurf_OnMuteChange(MediaTrack trackid, integer mute)
function reaper.CSurf_OnMuteChange(trackid, mute)
end


---Lua: boolean reaper.CSurf_OnMuteChangeEx(MediaTrack trackid, integer mute, boolean allowgang)
function reaper.CSurf_OnMuteChangeEx(trackid, mute, allowgang)
end


---Lua: number reaper.CSurf_OnPanChange(MediaTrack trackid, number pan, boolean relative)
function reaper.CSurf_OnPanChange(trackid, pan, relative)
end


---Lua: number reaper.CSurf_OnPanChangeEx(MediaTrack trackid, number pan, boolean relative, boolean allowGang)
function reaper.CSurf_OnPanChangeEx(trackid, pan, relative, allowGang)
end


---Lua: reaper.CSurf_OnPause()
function reaper.CSurf_OnPause()
end


---Lua: reaper.CSurf_OnPlay()
function reaper.CSurf_OnPlay()
end


---Lua: reaper.CSurf_OnPlayRateChange(number playrate)
function reaper.CSurf_OnPlayRateChange(playrate)
end


---Lua: boolean reaper.CSurf_OnRecArmChange(MediaTrack trackid, integer recarm)
function reaper.CSurf_OnRecArmChange(trackid, recarm)
end


---Lua: boolean reaper.CSurf_OnRecArmChangeEx(MediaTrack trackid, integer recarm, boolean allowgang)
function reaper.CSurf_OnRecArmChangeEx(trackid, recarm, allowgang)
end


---Lua: reaper.CSurf_OnRecord()
function reaper.CSurf_OnRecord()
end


---Lua: number reaper.CSurf_OnRecvPanChange(MediaTrack trackid, integer recv_index, number pan, boolean relative)
function reaper.CSurf_OnRecvPanChange(trackid, recv_index, pan, relative)
end


---Lua: number reaper.CSurf_OnRecvVolumeChange(MediaTrack trackid, integer recv_index, number volume, boolean relative)
function reaper.CSurf_OnRecvVolumeChange(trackid, recv_index, volume, relative)
end


---Lua: reaper.CSurf_OnRew(integer seekplay)
function reaper.CSurf_OnRew(seekplay)
end


---Lua: reaper.CSurf_OnRewFwd(integer seekplay, integer dir)
function reaper.CSurf_OnRewFwd(seekplay, dir)
end


---Lua: reaper.CSurf_OnScroll(integer xdir, integer ydir)
function reaper.CSurf_OnScroll(xdir, ydir)
end


---Lua: boolean reaper.CSurf_OnSelectedChange(MediaTrack trackid, integer selected)
function reaper.CSurf_OnSelectedChange(trackid, selected)
end


---Lua: number reaper.CSurf_OnSendPanChange(MediaTrack trackid, integer send_index, number pan, boolean relative)
function reaper.CSurf_OnSendPanChange(trackid, send_index, pan, relative)
end


---Lua: number reaper.CSurf_OnSendVolumeChange(MediaTrack trackid, integer send_index, number volume, boolean relative)
function reaper.CSurf_OnSendVolumeChange(trackid, send_index, volume, relative)
end


---Lua: boolean reaper.CSurf_OnSoloChange(MediaTrack trackid, integer solo)
function reaper.CSurf_OnSoloChange(trackid, solo)
end


---Lua: boolean reaper.CSurf_OnSoloChangeEx(MediaTrack trackid, integer solo, boolean allowgang)
function reaper.CSurf_OnSoloChangeEx(trackid, solo, allowgang)
end


---Lua: reaper.CSurf_OnStop()
function reaper.CSurf_OnStop()
end


---Lua: reaper.CSurf_OnTempoChange(number bpm)
function reaper.CSurf_OnTempoChange(bpm)
end


---Lua: reaper.CSurf_OnTrackSelection(MediaTrack trackid)
function reaper.CSurf_OnTrackSelection(trackid)
end


---Lua: number reaper.CSurf_OnVolumeChange(MediaTrack trackid, number volume, boolean relative)
function reaper.CSurf_OnVolumeChange(trackid, volume, relative)
end


---Lua: number reaper.CSurf_OnVolumeChangeEx(MediaTrack trackid, number volume, boolean relative, boolean allowGang)
function reaper.CSurf_OnVolumeChangeEx(trackid, volume, relative, allowGang)
end


---Lua: number reaper.CSurf_OnWidthChange(MediaTrack trackid, number width, boolean relative)
function reaper.CSurf_OnWidthChange(trackid, width, relative)
end


---Lua: number reaper.CSurf_OnWidthChangeEx(MediaTrack trackid, number width, boolean relative, boolean allowGang)
function reaper.CSurf_OnWidthChangeEx(trackid, width, relative, allowGang)
end


---Lua: reaper.CSurf_OnZoom(integer xdir, integer ydir)
function reaper.CSurf_OnZoom(xdir, ydir)
end


---Lua: reaper.CSurf_ResetAllCachedVolPanStates()
function reaper.CSurf_ResetAllCachedVolPanStates()
end


---Lua: reaper.CSurf_ScrubAmt(number amt)
function reaper.CSurf_ScrubAmt(amt)
end


---Lua: reaper.CSurf_SetAutoMode(integer mode, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetAutoMode(mode, ignoresurf)
end


---Lua: reaper.CSurf_SetPlayState(boolean play, boolean pause, boolean rec, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetPlayState(play, pause, rec, ignoresurf)
end


---Lua: reaper.CSurf_SetRepeatState(boolean rep, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetRepeatState(rep, ignoresurf)
end


---Lua: reaper.CSurf_SetSurfaceMute(MediaTrack trackid, boolean mute, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetSurfaceMute(trackid, mute, ignoresurf)
end


---Lua: reaper.CSurf_SetSurfacePan(MediaTrack trackid, number pan, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetSurfacePan(trackid, pan, ignoresurf)
end


---Lua: reaper.CSurf_SetSurfaceRecArm(MediaTrack trackid, boolean recarm, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetSurfaceRecArm(trackid, recarm, ignoresurf)
end


---Lua: reaper.CSurf_SetSurfaceSelected(MediaTrack trackid, boolean selected, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetSurfaceSelected(trackid, selected, ignoresurf)
end


---Lua: reaper.CSurf_SetSurfaceSolo(MediaTrack trackid, boolean solo, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetSurfaceSolo(trackid, solo, ignoresurf)
end


---Lua: reaper.CSurf_SetSurfaceVolume(MediaTrack trackid, number volume, IReaperControlSurface ignoresurf)
function reaper.CSurf_SetSurfaceVolume(trackid, volume, ignoresurf)
end


---Lua: reaper.CSurf_SetTrackListChange()
function reaper.CSurf_SetTrackListChange()
end


---Lua: MediaTrack reaper.CSurf_TrackFromID(integer idx, boolean mcpView)
function reaper.CSurf_TrackFromID(idx, mcpView)
end


---Lua: integer reaper.CSurf_TrackToID(MediaTrack track, boolean mcpView)
function reaper.CSurf_TrackToID(track, mcpView)
end


---Lua: number reaper.DB2SLIDER(number x)
function reaper.DB2SLIDER(x)
end


---Lua: boolean reaper.DeleteEnvelopePointRange(TrackEnvelope envelope, number time_start, number time_end)
---
---
---Delete a range of envelope points.
function reaper.DeleteEnvelopePointRange(envelope, time_start, time_end)
end


---Lua: boolean reaper.DeleteEnvelopePointRangeEx(TrackEnvelope envelope, integer autoitem_idx, number time_start, number time_end)
---
---
---Delete a range of envelope points. autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc.
function reaper.DeleteEnvelopePointRangeEx(envelope, autoitem_idx, time_start, time_end)
end


---Lua: reaper.DeleteExtState(string section, string key, boolean persist)
---
---
---Delete the extended state value for a specific section and key. persist=true means the value should remain deleted the next time REAPER is opened. See SetExtState
---, GetExtState
---, HasExtState
---.
function reaper.DeleteExtState(section, key, persist)
end


---Lua: boolean reaper.DeleteProjectMarker(ReaProject proj, integer markrgnindexnumber, boolean isrgn)
---
---
---Delete a marker.  proj==NULL for the active project.
function reaper.DeleteProjectMarker(proj, markrgnindexnumber, isrgn)
end


---Lua: boolean reaper.DeleteProjectMarkerByIndex(ReaProject proj, integer markrgnidx)
---
---
---Differs from DeleteProjectMarker only in that markrgnidx is 0 for the first marker/region, 1 for the next, etc (see EnumProjectMarkers3
---), rather than representing the displayed marker/region ID number (see SetProjectMarker4
---).
function reaper.DeleteProjectMarkerByIndex(proj, markrgnidx)
end


---Lua: integer reaper.DeleteTakeStretchMarkers(MediaItem_Take take, integer idx, optional number countIn)
---
---
---Deletes one or more stretch markers. Returns number of stretch markers deleted.
function reaper.DeleteTakeStretchMarkers(take, idx, countIn)
end


---Lua: boolean reaper.DeleteTempoTimeSigMarker(ReaProject project, integer markerindex)
---
---
---Delete a tempo/time signature marker.
function reaper.DeleteTempoTimeSigMarker(project, markerindex)
end


---Lua: reaper.DeleteTrack(MediaTrack tr)
---
---
---deletes a track
function reaper.DeleteTrack(tr)
end


---Lua: boolean reaper.DeleteTrackMediaItem(MediaTrack tr, MediaItem it)
function reaper.DeleteTrackMediaItem(tr, it)
end


---Lua: reaper.DestroyAudioAccessor(AudioAccessor accessor)
---
---
---Destroy an audio accessor. Must only call from the main thread. See CreateTakeAudioAccessor
---, CreateTrackAudioAccessor
---, GetAudioAccessorHash
---, GetAudioAccessorStartTime
---, GetAudioAccessorEndTime
---, GetAudioAccessorSamples
---.
function reaper.DestroyAudioAccessor(accessor)
end


---Lua: reaper.Dock_UpdateDockID(string ident_str, integer whichDock)
---
---
---updates preference for docker window ident_str to be in dock whichDock on next open
function reaper.Dock_UpdateDockID(ident_str, whichDock)
end


---Lua: integer retval, boolean isFloatingDocker = reaper.DockIsChildOfDock(HWND hwnd)
---
---
---returns dock index that contains hwnd, or -1
function reaper.DockIsChildOfDock(hwnd)
end


---Lua: reaper.DockWindowActivate(HWND hwnd)
function reaper.DockWindowActivate(hwnd)
end


---Lua: reaper.DockWindowAdd(HWND hwnd, string name, integer pos, boolean allowShow)
function reaper.DockWindowAdd(hwnd, name, pos, allowShow)
end


---Lua: reaper.DockWindowAddEx(HWND hwnd, string name, string identstr, boolean allowShow)
function reaper.DockWindowAddEx(hwnd, name, identstr, allowShow)
end


---Lua: reaper.DockWindowRefresh()
function reaper.DockWindowRefresh()
end


---Lua: reaper.DockWindowRefreshForHWND(HWND hwnd)
function reaper.DockWindowRefreshForHWND(hwnd)
end


---Lua: reaper.DockWindowRemove(HWND hwnd)
function reaper.DockWindowRemove(hwnd)
end


---Lua: boolean reaper.EditTempoTimeSigMarker(ReaProject project, integer markerindex)
---
---
---Open the tempo/time signature marker editor dialog.
function reaper.EditTempoTimeSigMarker(project, markerindex)
end


---Lua: numberrIn.left, numberrIn.top, numberrIn.right, numberrIn.bot = reaper.EnsureNotCompletelyOffscreen()
---
---
---call with a saved window rect for your window and it'll correct any positioning info.
function reaper.EnsureNotCompletelyOffscreen()
end


---Lua: string reaper.EnumerateFiles(string path, integer fileindex)
---
---
---List the files in the "path" directory. Returns NULL (or empty string, in Lua) when all files have been listed. See EnumerateSubdirectories
function reaper.EnumerateFiles(path, fileindex)
end


---Lua: string reaper.EnumerateSubdirectories(string path, integer subdirindex)
---
---
---List the subdirectories in the "path" directory. Returns NULL (or empty string, in Lua) when all subdirectories have been listed. See EnumerateFiles
function reaper.EnumerateSubdirectories(path, subdirindex)
end


---Lua: boolean retval, string str = reaper.EnumPitchShiftModes(integer mode)
---
---
---Start querying modes at 0, returns FALSE when no more modes possible, sets strOut to NULL if a mode is currently unsupported
function reaper.EnumPitchShiftModes(mode)
end


---Lua: string reaper.EnumPitchShiftSubModes(integer mode, integer submode)
---
---
---Returns submode name, or NULL
function reaper.EnumPitchShiftSubModes(mode, submode)
end


---Lua: integer retval, boolean isrgn, number pos, number rgnend, string name, number markrgnindexnumber = reaper.EnumProjectMarkers(integer idx)
function reaper.EnumProjectMarkers(idx)
end


---Lua: integer retval, boolean isrgn, number pos, number rgnend, string name, number markrgnindexnumber = reaper.EnumProjectMarkers2(ReaProject proj, integer idx)
function reaper.EnumProjectMarkers2(proj, idx)
end


---Lua: integer retval, boolean isrgn, number pos, number rgnend, string name, number markrgnindexnumber, number color = reaper.EnumProjectMarkers3(ReaProject proj, integer idx)
function reaper.EnumProjectMarkers3(proj, idx)
end


---Lua: ReaProject retval, string projfn = reaper.EnumProjects(integer idx, string projfn)
---
---
---idx=-1 for current project,projfn can be NULL if not interested in filename. use idx 0x40000000 for currently rendering project, if any.
function reaper.EnumProjects(idx, projfn)
end


---Lua: boolean retval, optional string key, optional string val = reaper.EnumProjExtState(ReaProject proj, string extname, integer idx)
---
---
---Enumerate the data stored with the project for a specific extname. Returns false when there is no more data. See SetProjExtState
---, GetProjExtState
---.
function reaper.EnumProjExtState(proj, extname, idx)
end


---Lua: MediaTrack reaper.EnumRegionRenderMatrix(ReaProject proj, integer regionindex, integer rendertrack)
---
---
---Enumerate which tracks will be rendered within this region when using the region render matrix. When called with rendertrack==0, the function returns the first track that will be rendered (which may be the master track); rendertrack==1 will return the next track rendered, and so on. The function returns NULL when there are no more tracks that will be rendered within this region.
function reaper.EnumRegionRenderMatrix(proj, regionindex, rendertrack)
end


---Lua: boolean retval, string programName = reaper.EnumTrackMIDIProgramNames(integer track, integer programNumber, string programName)
---
---
---returns false if there are no plugins on the track that support MIDI programs,or if all programs have been enumerated
function reaper.EnumTrackMIDIProgramNames(track, programNumber, programName)
end


---Lua: boolean retval, string programName = reaper.EnumTrackMIDIProgramNamesEx(ReaProject proj, MediaTrack track, integer programNumber, string programName)
---
---
---returns false if there are no plugins on the track that support MIDI programs,or if all programs have been enumerated
function reaper.EnumTrackMIDIProgramNamesEx(proj, track, programNumber, programName)
end


---Lua: integer retval, optional number value, optional number dVdS, optional number ddVdS, optional number dddVdS = reaper.Envelope_Evaluate(TrackEnvelope envelope, number time, number samplerate, integer samplesRequested)
---
---
---Get the effective envelope value at a given time position. samplesRequested is how long the caller expects until the next call to Envelope_Evaluate (often, the buffer block size). The return value is how many samples beyond that time position that the returned values are valid. dVdS is the change in value per sample (first derivative), ddVdS is the seond derivative, dddVdS is the third derivative. See GetEnvelopeScalingMode
---.
function reaper.Envelope_Evaluate(envelope, time, samplerate, samplesRequested)
end


---Lua: string buf = reaper.Envelope_FormatValue(TrackEnvelope env, number value)
---
---
---Formats the value of an envelope to a user-readable form
function reaper.Envelope_FormatValue(env, value)
end


---Lua: MediaItem_Take retval, optional number index, optional number index2 = reaper.Envelope_GetParentTake(TrackEnvelope env)
---
---
---If take envelope, gets the take from the envelope. If FX, indexOutOptional set to FX index, index2OutOptional set to parameter index, otherwise -1.
function reaper.Envelope_GetParentTake(env)
end


---Lua: MediaTrack retval, optional number index, optional number index2 = reaper.Envelope_GetParentTrack(TrackEnvelope env)
---
---
---If track envelope, gets the track from the envelope. If FX, indexOutOptional set to FX index, index2OutOptional set to parameter index, otherwise -1.
function reaper.Envelope_GetParentTrack(env)
end


---Lua: boolean reaper.Envelope_SortPoints(TrackEnvelope envelope)
---
---
---Sort envelope points by time. See SetEnvelopePoint
---, InsertEnvelopePoint
---.
function reaper.Envelope_SortPoints(envelope)
end


---Lua: boolean reaper.Envelope_SortPointsEx(TrackEnvelope envelope, integer autoitem_idx)
---
---
---Sort envelope points by time.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See SetEnvelopePoint
---, InsertEnvelopePoint
---.
function reaper.Envelope_SortPointsEx(envelope, autoitem_idx)
end


---Lua: string reaper.ExecProcess(string cmdline, integer timeoutmsec)
---
---
---Executes command line, returns NULL on total failure, otherwise the return value, a newline, and then the output of the command. If timeoutmsec is 0, command will be allowed to run indefinitely (recommended for large amounts of returned output). timeoutmsec is -1 for no wait/terminate, -2 for no wait and minimize
function reaper.ExecProcess(cmdline, timeoutmsec)
end


---Lua: boolean reaper.file_exists(string path)
---
---
---returns true if path points to a valid, readable file
function reaper.file_exists(path)
end


---Lua: integer reaper.FindTempoTimeSigMarker(ReaProject project, number time)
---
---
---Find the tempo/time signature marker that falls at or before this time position (the marker that is in effect as of this time position).
function reaper.FindTempoTimeSigMarker(project, time)
end


---Lua: string buf = reaper.format_timestr(number tpos, string buf)
---
---
---Format tpos (which is time in seconds) as hh:mm:ss.sss. See format_timestr_pos
---, format_timestr_len
---.
function reaper.format_timestr(tpos, buf)
end


---Lua: string buf = reaper.format_timestr_len(number tpos, string buf, number offset, integer modeoverride)
---
---
---time formatting mode overrides: -1=proj default.
---
---0=time
---
---1=measures.beats + time
---
---2=measures.beats
---
---3=seconds
---
---4=samples
---
---5=h:m:s:f
---
---offset is start of where the length will be calculated from
function reaper.format_timestr_len(tpos, buf, offset, modeoverride)
end


---Lua: string buf = reaper.format_timestr_pos(number tpos, string buf, integer modeoverride)
---
---
---time formatting mode overrides: -1=proj default.
---
---0=time
---
---1=measures.beats + time
---
---2=measures.beats
---
---3=seconds
---
---4=samples
---
---5=h:m:s:f
function reaper.format_timestr_pos(tpos, buf, modeoverride)
end


---Lua: string gGUID = reaper.genGuid(string gGUID)
function reaper.genGuid(gGUID)
end


---Lua: string reaper.get_ini_file()
---
---
---Get reaper.ini full filename.
function reaper.get_ini_file()
end


---Lua: MediaItem_Take reaper.GetActiveTake(MediaItem item)
---
---
---get the active take in this item
function reaper.GetActiveTake(item)
end


---Lua: integer reaper.GetAllProjectPlayStates(ReaProject ignoreProject)
---
---
---returns the bitwise OR of all project play states (1=playing, 2=pause, 4=recording)
function reaper.GetAllProjectPlayStates(ignoreProject)
end


---Lua: string reaper.GetAppVersion()
function reaper.GetAppVersion()
end


---Lua: integer retval, string sec = reaper.GetArmedCommand()
---
---
---gets the currently armed command and section name (returns 0 if nothing armed). section name is empty-string for main section.
function reaper.GetArmedCommand()
end


---Lua: number reaper.GetAudioAccessorEndTime(AudioAccessor accessor)
---
---
---Get the end time of the audio that can be returned from this accessor. See CreateTakeAudioAccessor
---, CreateTrackAudioAccessor
---, DestroyAudioAccessor
---, GetAudioAccessorHash
---, GetAudioAccessorStartTime
---, GetAudioAccessorSamples
---.
function reaper.GetAudioAccessorEndTime(accessor)
end


---Lua: string hashNeed128 = reaper.GetAudioAccessorHash(AudioAccessor accessor, string hashNeed128)
---
---
---Get a short hash string (128 chars or less) that will change only if the underlying samples change.  See CreateTakeAudioAccessor
---, CreateTrackAudioAccessor
---, DestroyAudioAccessor
---, GetAudioAccessorStartTime
---, GetAudioAccessorEndTime
---, GetAudioAccessorSamples
---.
function reaper.GetAudioAccessorHash(accessor, hashNeed128)
end


---Lua: integer reaper.GetAudioAccessorSamples(AudioAccessor accessor, integer samplerate, integer numchannels, number starttime_sec, integer numsamplesperchannel, reaper.array samplebuffer)
---
---
---Get a block of samples from the audio accessor. Samples are extracted immediately pre-FX, and returned interleaved (first sample of first channel, first sample of second channel...). Returns 0 if no audio, 1 if audio, -1 on error. See CreateTakeAudioAccessor
---, CreateTrackAudioAccessor
---, DestroyAudioAccessor
---, GetAudioAccessorHash
---, GetAudioAccessorStartTime
---, GetAudioAccessorEndTime
---.
---
---
---This function has special handling in Python, and only returns two objects, the API function return value, and the sample buffer. Example usage:
---
---tr = RPR_GetTrack(0, 0)
---aa = RPR_CreateTrackAudioAccessor(tr)
---buf = list([0]*2*1024) # 2 channels, 1024 samples each, initialized to zero
---pos = 0.0
---(ret, buf) = GetAudioAccessorSamples(aa, 44100, 2, pos, 1024, buf)
---# buf now holds the first 2*1024 audio samples from the track.
---# typically GetAudioAccessorSamples() would be called within a loop, increasing pos each time.
function reaper.GetAudioAccessorSamples(accessor, samplerate, numchannels, starttime_sec, numsamplesperchannel, samplebuffer)
end


---Lua: number reaper.GetAudioAccessorStartTime(AudioAccessor accessor)
---
---
---Get the start time of the audio that can be returned from this accessor. See CreateTakeAudioAccessor
---, CreateTrackAudioAccessor
---, DestroyAudioAccessor
---, GetAudioAccessorHash
---, GetAudioAccessorEndTime
---, GetAudioAccessorSamples
---.
function reaper.GetAudioAccessorStartTime(accessor)
end


---Lua: integer reaper.GetConfigWantsDock(string ident_str)
---
---
---gets the dock ID desired by ident_str, if any
function reaper.GetConfigWantsDock(ident_str)
end


---Lua: ReaProject reaper.GetCurrentProjectInLoadSave()
---
---
---returns current project if in load/save (usually only used from project_config_extension_t)
function reaper.GetCurrentProjectInLoadSave()
end


---Lua: integer reaper.GetCursorContext()
---
---
---return the current cursor context: 0 if track panels, 1 if items, 2 if envelopes, otherwise unknown
function reaper.GetCursorContext()
end


---Lua: integer reaper.GetCursorContext2(boolean want_last_valid)
---
---
---0 if track panels, 1 if items, 2 if envelopes, otherwise unknown (unlikely when want_last_valid is true)
function reaper.GetCursorContext2(want_last_valid)
end


---Lua: number reaper.GetCursorPosition()
---
---
---edit cursor position
function reaper.GetCursorPosition()
end


---Lua: number reaper.GetCursorPositionEx(ReaProject proj)
---
---
---edit cursor position
function reaper.GetCursorPositionEx(proj)
end


---Lua: integer reaper.GetDisplayedMediaItemColor(MediaItem item)
---
---
---see GetDisplayedMediaItemColor2
---.
function reaper.GetDisplayedMediaItemColor(item)
end


---Lua: integer reaper.GetDisplayedMediaItemColor2(MediaItem item, MediaItem_Take take)
---
---
---Returns the custom take, item, or track color that is used (according to the user preference) to color the media item. The returned color is OS dependent|0x01000000 (i.e. ColorToNative(r,g,b)|0x01000000), so a return of zero means "no color", not black.
function reaper.GetDisplayedMediaItemColor2(item, take)
end


---Lua: boolean retval, string buf = reaper.GetEnvelopeName(TrackEnvelope env, string buf)
function reaper.GetEnvelopeName(env, buf)
end


---Lua: boolean retval, optional number time, optional number value, optional number shape, optional number tension, optional boolean selected = reaper.GetEnvelopePoint(TrackEnvelope envelope, integer ptidx)
---
---
---Get the attributes of an envelope point. See GetEnvelopePointByTime
---, SetEnvelopePoint
---.
function reaper.GetEnvelopePoint(envelope, ptidx)
end


---Lua: integer reaper.GetEnvelopePointByTime(TrackEnvelope envelope, number time)
---
---
---Returns the envelope point at or immediately prior to the given time position. See GetEnvelopePoint
---, SetEnvelopePoint
---, Envelope_Evaluate
---.
function reaper.GetEnvelopePointByTime(envelope, time)
end


---Lua: integer reaper.GetEnvelopePointByTimeEx(TrackEnvelope envelope, integer autoitem_idx, number time)
---
---
---Returns the envelope point at or immediately prior to the given time position.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePoint
---, SetEnvelopePoint
---, Envelope_Evaluate
---.
function reaper.GetEnvelopePointByTimeEx(envelope, autoitem_idx, time)
end


---Lua: boolean retval, optional number time, optional number value, optional number shape, optional number tension, optional boolean selected = reaper.GetEnvelopePointEx(TrackEnvelope envelope, integer autoitem_idx, integer ptidx)
---
---
---Get the attributes of an envelope point.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePointByTime
---, SetEnvelopePoint
---.
function reaper.GetEnvelopePointEx(envelope, autoitem_idx, ptidx)
end


---Lua: integer reaper.GetEnvelopeScalingMode(TrackEnvelope env)
---
---
---Returns the envelope scaling mode: 0=no scaling, 1=fader scaling. All API functions deal with raw envelope point values, to convert raw from/to scaled values see ScaleFromEnvelopeMode
---, ScaleToEnvelopeMode
---.
function reaper.GetEnvelopeScalingMode(env)
end


---Lua: boolean retval, string str = reaper.GetEnvelopeStateChunk(TrackEnvelope env, string str, boolean isundo)
---
---
---Gets the RPPXML state of an envelope, returns true if successful. Undo flag is a performance/caching hint.
function reaper.GetEnvelopeStateChunk(env, str, isundo)
end


---Lua: string reaper.GetExePath()
---
---
---returns path of REAPER.exe (not including EXE), i.e. C:\Program Files\REAPER
function reaper.GetExePath()
end


---Lua: string reaper.GetExtState(string section, string key)
---
---
---Get the extended state value for a specific section and key. See SetExtState
---, DeleteExtState
---, HasExtState
---.
function reaper.GetExtState(section, key)
end


---Lua: integer retval, number tracknumber, number itemnumber, number fxnumber = reaper.GetFocusedFX()
---
---
---Returns 1 if a track FX window has focus, 2 if an item FX window has focus, 0 if no FX window has focus. tracknumber==0 means the master track, 1 means track 1, etc. itemnumber and fxnumber are zero-based. If item FX, fxnumber will have the high word be the take index, the low word the FX index. See GetLastTouchedFX
---.
function reaper.GetFocusedFX()
end


---Lua: integer reaper.GetFreeDiskSpaceForRecordPath(ReaProject proj, integer pathidx)
---
---
---returns free disk space in megabytes, pathIdx 0 for normal, 1 for alternate.
function reaper.GetFreeDiskSpaceForRecordPath(proj, pathidx)
end


---Lua: TrackEnvelope reaper.GetFXEnvelope(MediaTrack track, integer fxindex, integer parameterindex, boolean create)
---
---
---Returns the FX parameter envelope. If the envelope does not exist and create=true, the envelope will be created.
function reaper.GetFXEnvelope(track, fxindex, parameterindex, create)
end


---Lua: integer reaper.GetGlobalAutomationOverride()
---
---
---return -1=no override, 0=trim/read, 1=read, 2=touch, 3=write, 4=latch, 5=bypass
function reaper.GetGlobalAutomationOverride()
end


---Lua: number reaper.GetHZoomLevel()
---
---
---returns pixels/second
function reaper.GetHZoomLevel()
end


---Lua: string reaper.GetInputChannelName(integer channelIndex)
function reaper.GetInputChannelName(channelIndex)
end


---Lua: number inputlatency, number outputLatency = reaper.GetInputOutputLatency()
---
---
---Gets the audio device input/output latency in samples
function reaper.GetInputOutputLatency()
end


---Lua: number, PCM_source which_item, number flags = reaper.GetItemEditingTime2()
---
---
---returns time of relevant edit, set which_item to the pcm_source (if applicable), flags (if specified) will be set to 1 for edge resizing, 2 for fade change, 4 for item move
function reaper.GetItemEditingTime2()
end


---Lua: ReaProject reaper.GetItemProjectContext(MediaItem item)
function reaper.GetItemProjectContext(item)
end


---Lua: boolean retval, string str = reaper.GetItemStateChunk(MediaItem item, string str, boolean isundo)
---
---
---Gets the RPPXML state of an item, returns true if successful. Undo flag is a performance/caching hint.
function reaper.GetItemStateChunk(item, str, isundo)
end


---Lua: string reaper.GetLastColorThemeFile()
function reaper.GetLastColorThemeFile()
end


---Lua: number markeridx, number regionidx = reaper.GetLastMarkerAndCurRegion(ReaProject proj, number time)
---
---
---Get the last project marker before time, and/or the project region that includes time. markeridx and regionidx are returned not necessarily as the displayed marker/region index, but as the index that can be passed to EnumProjectMarkers. Either or both of markeridx and regionidx may be NULL. See EnumProjectMarkers
---.
function reaper.GetLastMarkerAndCurRegion(proj, time)
end


---Lua: boolean retval, number tracknumber, number fxnumber, number paramnumber = reaper.GetLastTouchedFX()
---
---
---Returns true if the last touched FX parameter is valid, false otherwise. tracknumber==0 means the master track, 1 means track 1, etc. fxnumber and paramnumber are zero-based. See GetFocusedFX
---.
function reaper.GetLastTouchedFX()
end


---Lua: MediaTrack reaper.GetLastTouchedTrack()
function reaper.GetLastTouchedTrack()
end


---Lua: HWND reaper.GetMainHwnd()
function reaper.GetMainHwnd()
end


---Lua: integer reaper.GetMasterMuteSoloFlags()
---
---
---&1=master mute,&2=master solo. This is deprecated as you can just query the master track as well.
function reaper.GetMasterMuteSoloFlags()
end


---Lua: MediaTrack reaper.GetMasterTrack(ReaProject proj)
function reaper.GetMasterTrack(proj)
end


---Lua: integer reaper.GetMasterTrackVisibility()
---
---
---returns &1 if the master track is visible in the TCP, &2 if visible in the mixer. See SetMasterTrackVisibility
---.
function reaper.GetMasterTrackVisibility()
end


---Lua: integer reaper.GetMaxMidiInputs()
---
---
---returns max dev for midi inputs/outputs
function reaper.GetMaxMidiInputs()
end


---Lua: integer reaper.GetMaxMidiOutputs()
function reaper.GetMaxMidiOutputs()
end


---Lua: MediaItem reaper.GetMediaItem(ReaProject proj, integer itemidx)
---
---
---get an item from a project by item count (zero-based) (proj=0 for active project)
function reaper.GetMediaItem(proj, itemidx)
end


---Lua: MediaTrack reaper.GetMediaItem_Track(MediaItem item)
---
---
---Get parent track of media item
function reaper.GetMediaItem_Track(item)
end


---Lua: number reaper.GetMediaItemInfo_Value(MediaItem item, string parmname)
---
---
---Get media item numerical-value attributes.
---
---B_MUTE : bool * to muted state
---
---B_LOOPSRC : bool * to loop source
---
---B_ALLTAKESPLAY : bool * to all takes play
---
---B_UISEL : bool * to ui selected
---
---C_BEATATTACHMODE : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsosonly
---
---C_LOCK : char * to one char of lock flags (&1 is locked, currently)
---
---D_VOL : double * of item volume (volume bar)
---
---D_POSITION : double * of item position (seconds)
---
---D_LENGTH : double * of item length (seconds)
---
---D_SNAPOFFSET : double * of item snap offset (seconds)
---
---D_FADEINLEN : double * of item fade in length (manual, seconds)
---
---D_FADEOUTLEN : double * of item fade out length (manual, seconds)
---
---D_FADEINDIR : double * of item fade in curve [-1; 1]
---
---D_FADEOUTDIR : double * of item fade out curve [-1; 1]
---
---D_FADEINLEN_AUTO : double * of item autofade in length (seconds, -1 for no autofade set)
---
---D_FADEOUTLEN_AUTO : double * of item autofade out length (seconds, -1 for no autofade set)
---
---C_FADEINSHAPE : int * to fadein shape, 0=linear, ...
---
---C_FADEOUTSHAPE : int * to fadeout shape
---
---I_GROUPID : int * to group ID (0 = no group)
---
---I_LASTY : int * to last y position in track (readonly)
---
---I_LASTH : int * to last height in track (readonly)
---
---I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
---
---I_CURTAKE : int * to active take
---
---IP_ITEMNUMBER : int, item number within the track (read-only, returns the item number directly)
---
---F_FREEMODE_Y : float * to free mode y position (0..1)
---
---F_FREEMODE_H : float * to free mode height (0..1)
---
---P_TRACK : MediaTrack * (read only)
function reaper.GetMediaItemInfo_Value(item, parmname)
end


---Lua: integer reaper.GetMediaItemNumTakes(MediaItem item)
function reaper.GetMediaItemNumTakes(item)
end


---Lua: MediaItem_Take reaper.GetMediaItemTake(MediaItem item, integer tk)
function reaper.GetMediaItemTake(item, tk)
end


---Lua: MediaItem reaper.GetMediaItemTake_Item(MediaItem_Take take)
---
---
---Get parent item of media item take
function reaper.GetMediaItemTake_Item(take)
end


---Lua: integer reaper.GetMediaItemTake_Peaks(MediaItem_Take take, number peakrate, number starttime, integer numchannels, integer numsamplesperchannel, integer want_extra_type, reaper.array buf)
---
---
---Gets block of peak samples to buf. Note that the peak samples are interleaved, but in two or three blocks (maximums, then minimums, then extra). Return value has 20 bits of returned sample count, then 4 bits of output_mode (0xf00000), then a bit to signify whether extra_type was available (0x1000000). extra_type can be 115 ('s') for spectral information, which will return peak samples as integers with the low 15 bits frequency, next 14 bits tonality.
function reaper.GetMediaItemTake_Peaks(take, peakrate, starttime, numchannels, numsamplesperchannel, want_extra_type, buf)
end


---Lua: PCM_source reaper.GetMediaItemTake_Source(MediaItem_Take take)
---
---
---Get media source of media item take
function reaper.GetMediaItemTake_Source(take)
end


---Lua: MediaTrack reaper.GetMediaItemTake_Track(MediaItem_Take take)
---
---
---Get parent track of media item take
function reaper.GetMediaItemTake_Track(take)
end


---Lua: MediaItem_Take reaper.GetMediaItemTakeByGUID(ReaProject project, string guidGUID)
function reaper.GetMediaItemTakeByGUID(project, guidGUID)
end


---Lua: number reaper.GetMediaItemTakeInfo_Value(MediaItem_Take take, string parmname)
---
---
---Get media item take numerical-value attributes.
---
---D_STARTOFFS : double *, start offset in take of item
---
---D_VOL : double *, take volume
---
---D_PAN : double *, take pan
---
---D_PANLAW : double *, take pan law (-1.0=default, 0.5=-6dB, 1.0=+0dB, etc)
---
---D_PLAYRATE : double *, take playrate (1.0=normal, 2.0=doublespeed, etc)
---
---D_PITCH : double *, take pitch adjust (in semitones, 0.0=normal, +12 = one octave up, etc)
---
---B_PPITCH, bool *, preserve pitch when changing rate
---
---I_CHANMODE, int *, channel mode (0=normal, 1=revstereo, 2=downmix, 3=l, 4=r)
---
---I_PITCHMODE, int *, pitch shifter mode, -1=proj default, otherwise high word=shifter low word = parameter
---
---I_CUSTOMCOLOR : int *, custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
---
---IP_TAKENUMBER : int, take number within the item (read-only, returns the take number directly)
---
---P_TRACK : pointer to MediaTrack (read-only)
---
---P_ITEM : pointer to MediaItem (read-only)
---
---P_SOURCE : PCM_source *. Note that if setting this, you should first retrieve the old source, set the new, THEN delete the old.
function reaper.GetMediaItemTakeInfo_Value(take, parmname)
end


---Lua: MediaTrack reaper.GetMediaItemTrack(MediaItem item)
function reaper.GetMediaItemTrack(item)
end


---Lua: string filenamebuf = reaper.GetMediaSourceFileName(PCM_source source, string filenamebuf)
---
---
---Copies the media source filename to typebuf. Note that in-project MIDI media sources have no associated filename. See GetMediaSourceParent
---.
function reaper.GetMediaSourceFileName(source, filenamebuf)
end


---Lua: number retval, boolean lengthIsQN = reaper.GetMediaSourceLength(PCM_source source)
---
---
---Returns the length of the source media. If the media source is beat-based, the length will be in quarter notes, otherwise it will be in seconds.
function reaper.GetMediaSourceLength(source)
end


---Lua: integer reaper.GetMediaSourceNumChannels(PCM_source source)
---
---
---Returns the number of channels in the source media.
function reaper.GetMediaSourceNumChannels(source)
end


---Lua: PCM_source reaper.GetMediaSourceParent(PCM_source src)
---
---
---Returns the parent source, or NULL if src is the root source. This can be used to retrieve the parent properties of sections or reversed sources for example.
function reaper.GetMediaSourceParent(src)
end


---Lua: integer reaper.GetMediaSourceSampleRate(PCM_source source)
---
---
---Returns the sample rate. MIDI source media will return zero.
function reaper.GetMediaSourceSampleRate(source)
end


---Lua: string typebuf = reaper.GetMediaSourceType(PCM_source source, string typebuf)
---
---
---copies the media source type ("WAV", "MIDI", etc) to typebuf
function reaper.GetMediaSourceType(source, typebuf)
end


---Lua: number reaper.GetMediaTrackInfo_Value(MediaTrack tr, string parmname)
---
---
---Get track numerical-value attributes.
---
---B_MUTE : bool * : mute flag
---
---B_PHASE : bool * : invert track phase
---
---IP_TRACKNUMBER : int : track number (returns zero if not found, -1 for master track) (read-only, returns the int directly)
---
---I_SOLO : int * : 0=not soloed, 1=solo, 2=soloed in place. also: 5=solo-safe solo, 6=solo-safe soloed in place
---
---I_FXEN : int * : 0=fx bypassed, nonzero = fx active
---
---I_RECARM : int * : 0=not record armed, 1=record armed
---
---I_RECINPUT : int * : record input. <0 = no input, 0..n = mono hardware input, 512+n = rearoute input, 1024 set for stereo input pair. 4096 set for MIDI input, if set, then low 5 bits represent channel (0=all, 1-16=only chan), then next 6 bits represent physical input (63=all, 62=VKB)
---
---I_RECMODE : int * : record mode (0=input, 1=stereo out, 2=none, 3=stereo out w/latcomp, 4=midi output, 5=mono out, 6=mono out w/ lat comp, 7=midi overdub, 8=midi replace
---
---I_RECMON : int * : record monitor (0=off, 1=normal, 2=not when playing (tapestyle))
---
---I_RECMONITEMS : int * : monitor items while recording (0=off, 1=on)
---
---I_AUTOMODE : int * : track automation mode (0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
---
---I_NCHAN : int * : number of track channels, must be 2-64, even
---
---I_SELECTED : int * : track selected? 0 or 1
---
---I_WNDH : int * : current TCP window height (Read-only)
---
---I_FOLDERDEPTH : int * : folder depth change (0=normal, 1=track is a folder parent, -1=track is the last in the innermost folder, -2=track is the last in the innermost and next-innermost folders, etc
---
---I_FOLDERCOMPACT : int * : folder compacting (only valid on folders), 0=normal, 1=small, 2=tiny children
---
---I_MIDIHWOUT : int * : track midi hardware output index (<0 for disabled, low 5 bits are which channels (0=all, 1-16), next 5 bits are output device index (0-31))
---
---I_PERFFLAGS : int * : track perf flags (&1=no media buffering, &2=no anticipative FX)
---
---I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
---
---I_HEIGHTOVERRIDE : int * : custom height override for TCP window. 0 for none, otherwise size in pixels
---
---B_HEIGHTLOCK : bool * : track height lock (must set I_HEIGHTOVERRIDE before locking)
---
---D_VOL : double * : trim volume of track (0 (-inf)..1 (+0dB) .. 2 (+6dB) etc ..)
---
---D_PAN : double * : trim pan of track (-1..1)
---
---D_WIDTH : double * : width of track (-1..1)
---
---D_DUALPANL : double * : dualpan position 1 (-1..1), only if I_PANMODE==6
---
---D_DUALPANR : double * : dualpan position 2 (-1..1), only if I_PANMODE==6
---
---I_PANMODE : int * : pan mode (0 = classic 3.x, 3=new balance, 5=stereo pan, 6 = dual pan)
---
---D_PANLAW : double * : pan law of track. <0 for project default, 1.0 for +0dB, etc
---
---P_ENV : read only, returns TrackEnvelope *, setNewValue=<VOLENV, <PANENV, etc
---
---B_SHOWINMIXER : bool * : show track panel in mixer -- do not use on master
---
---B_SHOWINTCP : bool * : show track panel in tcp -- do not use on master
---
---B_MAINSEND : bool * : track sends audio to parent
---
---C_MAINSEND_OFFS : char * : track send to parent channel offset
---
---B_FREEMODE : bool * : track free-mode enabled (requires UpdateTimeline() after changing etc)
---
---C_BEATATTACHMODE : char * : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsposonly
---
---F_MCP_FXSEND_SCALE : float * : scale of fx+send area in MCP (0.0=smallest allowed, 1=max allowed)
---
---F_MCP_SENDRGN_SCALE : float * : scale of send area as proportion of the fx+send total area (0=min allow, 1=max)
---
---P_PARTRACK : MediaTrack * : parent track (read-only)
---
---P_PROJECT : ReaProject * : parent project (read-only)
function reaper.GetMediaTrackInfo_Value(tr, parmname)
end


---Lua: boolean retval, string nameout = reaper.GetMIDIInputName(integer dev, string nameout)
---
---
---returns true if device present
function reaper.GetMIDIInputName(dev, nameout)
end


---Lua: boolean retval, string nameout = reaper.GetMIDIOutputName(integer dev, string nameout)
---
---
---returns true if device present
function reaper.GetMIDIOutputName(dev, nameout)
end


---Lua: MediaTrack reaper.GetMixerScroll()
---
---
---Get the leftmost track visible in the mixer
function reaper.GetMixerScroll()
end


---Lua: string action = reaper.GetMouseModifier(string context, integer modifier_flag, string action)
---
---
---Get the current mouse modifier assignment for a specific modifier key assignment, in a specific context.
---
---action will be filled in with the command ID number for a built-in mouse modifier
---
---or built-in REAPER command ID, or the custom action ID string.
---
---See SetMouseModifier
--- for more information.
function reaper.GetMouseModifier(context, modifier_flag, action)
end


---Lua: number x, number y = reaper.GetMousePosition()
---
---
---get mouse position in screen coordinates
function reaper.GetMousePosition()
end


---Lua: integer reaper.GetNumAudioInputs()
---
---
---Return number of normal audio hardware inputs available
function reaper.GetNumAudioInputs()
end


---Lua: integer reaper.GetNumAudioOutputs()
---
---
---Return number of normal audio hardware outputs available
function reaper.GetNumAudioOutputs()
end


---Lua: integer reaper.GetNumMIDIInputs()
---
---
---returns max number of real midi hardware inputs
function reaper.GetNumMIDIInputs()
end


---Lua: integer reaper.GetNumMIDIOutputs()
---
---
---returns max number of real midi hardware outputs
function reaper.GetNumMIDIOutputs()
end


---Lua: integer reaper.GetNumTracks()
function reaper.GetNumTracks()
end


---Lua: string reaper.GetOS()
---
---
---Returns "Win32", "Win64", "OSX32", "OSX64", or "Other".
function reaper.GetOS()
end


---Lua: string reaper.GetOutputChannelName(integer channelIndex)
function reaper.GetOutputChannelName(channelIndex)
end


---Lua: number reaper.GetOutputLatency()
---
---
---returns output latency in seconds
function reaper.GetOutputLatency()
end


---Lua: MediaTrack reaper.GetParentTrack(MediaTrack track)
function reaper.GetParentTrack(track)
end


---Lua: string buf = reaper.GetPeakFileName(string fn, string buf)
---
---
---get the peak file name for a given file (can be either filename.reapeaks,or a hashed filename in another path)
function reaper.GetPeakFileName(fn, buf)
end


---Lua: string buf = reaper.GetPeakFileNameEx(string fn, string buf, boolean forWrite)
---
---
---get the peak file name for a given file (can be either filename.reapeaks,or a hashed filename in another path)
function reaper.GetPeakFileNameEx(fn, buf, forWrite)
end


---Lua: string buf = reaper.GetPeakFileNameEx2(string fn, string buf, boolean forWrite, string peaksfileextension)
---
---
---Like GetPeakFileNameEx, but you can specify peaksfileextension such as ".reapeaks"
function reaper.GetPeakFileNameEx2(fn, buf, forWrite, peaksfileextension)
end


---Lua: number reaper.GetPlayPosition()
---
---
---returns latency-compensated actual-what-you-hear position
function reaper.GetPlayPosition()
end


---Lua: number reaper.GetPlayPosition2()
---
---
---returns position of next audio block being processed
function reaper.GetPlayPosition2()
end


---Lua: number reaper.GetPlayPosition2Ex(ReaProject proj)
---
---
---returns position of next audio block being processed
function reaper.GetPlayPosition2Ex(proj)
end


---Lua: number reaper.GetPlayPositionEx(ReaProject proj)
---
---
---returns latency-compensated actual-what-you-hear position
function reaper.GetPlayPositionEx(proj)
end


---Lua: integer reaper.GetPlayState()
---
---
---&1=playing,&2=pause,&=4 is recording
function reaper.GetPlayState()
end


---Lua: integer reaper.GetPlayStateEx(ReaProject proj)
---
---
---&1=playing,&2=pause,&=4 is recording
function reaper.GetPlayStateEx(proj)
end


---Lua: number reaper.GetProjectLength(ReaProject proj)
---
---
---returns length of project (maximum of end of media item, markers, end of regions, tempo map
function reaper.GetProjectLength(proj)
end


---Lua: string buf = reaper.GetProjectName(ReaProject proj, string buf)
function reaper.GetProjectName(proj, buf)
end


---Lua: string buf = reaper.GetProjectPath(string buf)
function reaper.GetProjectPath(buf)
end


---Lua: string buf = reaper.GetProjectPathEx(ReaProject proj, string buf)
function reaper.GetProjectPathEx(proj, buf)
end


---Lua: integer reaper.GetProjectStateChangeCount(ReaProject proj)
---
---
---returns an integer that changes when the project state changes
function reaper.GetProjectStateChangeCount(proj)
end


---Lua: number reaper.GetProjectTimeOffset(ReaProject proj, boolean rndframe)
---
---
---Gets project time offset in seconds (project settings - project start time). If rndframe is true, the offset is rounded to a multiple of the project frame size.
function reaper.GetProjectTimeOffset(proj, rndframe)
end


---Lua: number bpm, number bpi = reaper.GetProjectTimeSignature()
---
---
---deprecated
function reaper.GetProjectTimeSignature()
end


---Lua: number bpm, number bpi = reaper.GetProjectTimeSignature2(ReaProject proj)
---
---
---Gets basic time signature (beats per minute, numerator of time signature in bpi)
---
---this does not reflect tempo envelopes but is purely what is set in the project settings.
function reaper.GetProjectTimeSignature2(proj)
end


---Lua: integer retval, string val = reaper.GetProjExtState(ReaProject proj, string extname, string key)
---
---
---Get the value previously associated with this extname and key, the last time the project was saved. See SetProjExtState
---, EnumProjExtState
---.
function reaper.GetProjExtState(proj, extname, key)
end


---Lua: string reaper.GetResourcePath()
---
---
---returns path where ini files are stored, other things are in subdirectories.
function reaper.GetResourcePath()
end


---Lua: TrackEnvelope reaper.GetSelectedEnvelope(ReaProject proj)
---
---
---get the currently selected envelope, returns 0 if no envelope is selected
function reaper.GetSelectedEnvelope(proj)
end


---Lua: MediaItem reaper.GetSelectedMediaItem(ReaProject proj, integer selitem)
---
---
---get a selected item by selected item count (zero-based) (proj=0 for active project)
function reaper.GetSelectedMediaItem(proj, selitem)
end


---Lua: MediaTrack reaper.GetSelectedTrack(ReaProject proj, integer seltrackidx)
---
---
---Get a selected track from a project (proj=0 for active project) by selected track count (zero-based). This function ignores the master track, see GetSelectedTrack2
---.
function reaper.GetSelectedTrack(proj, seltrackidx)
end


---Lua: MediaTrack reaper.GetSelectedTrack2(ReaProject proj, integer seltrackidx, boolean wantmaster)
---
---
---Get a selected track from a project (proj=0 for active project) by selected track count (zero-based).
function reaper.GetSelectedTrack2(proj, seltrackidx, wantmaster)
end


---Lua: TrackEnvelope reaper.GetSelectedTrackEnvelope(ReaProject proj)
---
---
---get the currently selected track envelope, returns 0 if no envelope is selected
function reaper.GetSelectedTrackEnvelope(proj)
end


---Lua: number start_time, number end_time = reaper.GetSet_ArrangeView2(ReaProject proj, boolean isSet, integer screen_x_start, integer screen_x_end)
---
---
---Gets or sets the arrange view start/end time for screen coordinates. use screen_x_start=screen_x_end=0 to use the full arrange view's start/end time
function reaper.GetSet_ArrangeView2(proj, isSet, screen_x_start, screen_x_end)
end


---Lua: number start, number end = reaper.GetSet_LoopTimeRange(boolean isSet, boolean isLoop, number start, number end, boolean allowautoseek)
function reaper.GetSet_LoopTimeRange(isSet, isLoop, start, End, allowautoseek)
end


---Lua: number start, number end = reaper.GetSet_LoopTimeRange2(ReaProject proj, boolean isSet, boolean isLoop, number start, number end, boolean allowautoseek)
function reaper.GetSet_LoopTimeRange2(proj, isSet, isLoop, start, End, allowautoseek)
end


---Lua: number reaper.GetSetAutomationItemInfo(TrackEnvelope env, integer autoitem_idx, string desc, number value, boolean is_set)
---
---
---Get or set automation item information. autoitem_idx==0 for the first automation item on an envelope, 1 for the second item, etc. desc can be any of the following:
---
---D_POOL_ID: double *, automation item pool ID (as an integer); edits are propagated to all other automation items that share a pool ID
---
---D_POSITION: double *, automation item timeline position in seconds
---
---D_LENGTH: double *, automation item length in seconds
---
---D_STARTOFFS: double *, automation item start offset in seconds
---
---D_PLAYRATE: double *, automation item playback rate
---
---D_BASELINE: double *, automation item baseline value in the range [0,1]
---
---D_AMPLITUDE: double *, automation item amplitude in the range [-1,1]
---
---D_LOOPSRC: double *, nonzero if the automation item contents are looped
---
---D_UISEL: double *, nonzero if the automation item is selected in the arrange view
function reaper.GetSetAutomationItemInfo(env, autoitem_idx, desc, value, is_set)
end


---Lua: boolean retval, string str = reaper.GetSetEnvelopeState(TrackEnvelope env, string str)
---
---
---deprecated -- see SetEnvelopeStateChunk
---, GetEnvelopeStateChunk
function reaper.GetSetEnvelopeState(env, str)
end


---Lua: boolean retval, string str = reaper.GetSetEnvelopeState2(TrackEnvelope env, string str, boolean isundo)
---
---
---deprecated -- see SetEnvelopeStateChunk
---, GetEnvelopeStateChunk
function reaper.GetSetEnvelopeState2(env, str, isundo)
end


---Lua: boolean retval, string str = reaper.GetSetItemState(MediaItem item, string str)
---
---
---deprecated -- see SetItemStateChunk
---, GetItemStateChunk
function reaper.GetSetItemState(item, str)
end


---Lua: boolean retval, string str = reaper.GetSetItemState2(MediaItem item, string str, boolean isundo)
---
---
---deprecated -- see SetItemStateChunk
---, GetItemStateChunk
function reaper.GetSetItemState2(item, str, isundo)
end


---Lua: boolean retval, string stringNeedBig = reaper.GetSetMediaItemInfo_String(MediaItem item, string parmname, string stringNeedBig, boolean setNewValue)
---
---
---Gets/sets an item attribute string:
---
---P_NOTES : char * : item note text (do not write to returned pointer, use setNewValue to update)
---
---GUID : GUID * : 16-byte GUID, can query or update. If using a _String() function, GUID is a string {xyz-...}.
function reaper.GetSetMediaItemInfo_String(item, parmname, stringNeedBig, setNewValue)
end


---Lua: boolean retval, string stringNeedBig = reaper.GetSetMediaItemTakeInfo_String(MediaItem_Take tk, string parmname, string stringNeedBig, boolean setNewValue)
---
---
---Gets/sets a take attribute string:
---
---P_NAME : char * to take name
---
---GUID : GUID * : 16-byte GUID, can query or update. If using a _String() function, GUID is a string {xyz-...}.
function reaper.GetSetMediaItemTakeInfo_String(tk, parmname, stringNeedBig, setNewValue)
end


---Lua: boolean retval, string stringNeedBig = reaper.GetSetMediaTrackInfo_String(MediaTrack tr, string parmname, string stringNeedBig, boolean setNewValue)
---
---
---Get or set track string attributes.
---
---P_NAME : char * : track name (on master returns NULL)
---
---P_ICON : const char * : track icon (full filename, or relative to resource_path/data/track_icons)
---
---P_MCP_LAYOUT : const char * : layout name
---
---P_TCP_LAYOUT : const char * : layout name
---
---GUID : GUID * : 16-byte GUID, can query or update. If using a _String() function, GUID is a string {xyz-...}.
function reaper.GetSetMediaTrackInfo_String(tr, parmname, stringNeedBig, setNewValue)
end


---Lua: string author = reaper.GetSetProjectAuthor(ReaProject proj, boolean set, string author)
---
---
---gets or sets project author, author_sz is ignored when setting
function reaper.GetSetProjectAuthor(proj, set, author)
end


---Lua: integer retval, optional number divisionIn, optional number swingmodeIn, optional number swingamtIn = reaper.GetSetProjectGrid(ReaProject project, boolean set)
---
---
---Get or set the arrange view grid division. 0.25=quarter note, 1.0/3.0=half note triplet, etc. swingmode can be 1 for swing enabled, swingamt is -1..1. Returns grid configuration flags
function reaper.GetSetProjectGrid(project, set)
end


---Lua: string notes = reaper.GetSetProjectNotes(ReaProject proj, boolean set, string notes)
---
---
---gets or sets project notes, notesNeedBig_sz is ignored when setting
function reaper.GetSetProjectNotes(proj, set, notes)
end


---Lua: integer reaper.GetSetRepeat(integer val)
---
---
----1 == query,0=clear,1=set,>1=toggle . returns new value
function reaper.GetSetRepeat(val)
end


---Lua: integer reaper.GetSetRepeatEx(ReaProject proj, integer val)
---
---
----1 == query,0=clear,1=set,>1=toggle . returns new value
function reaper.GetSetRepeatEx(proj, val)
end


---Lua: integer reaper.GetSetTrackGroupMembership(MediaTrack tr, string groupname, integer setmask, integer setvalue)
---
---
---Gets or modifies the group membership for a track. Returns group state prior to call (each bit represents one of the 32 group numbers). if setmask has bits set, those bits in setvalue will be applied to group. Group can be one of:
---
---VOLUME_MASTER
---
---VOLUME_SLAVE
---
---VOLUME_VCA_MASTER
---
---VOLUME_VCA_SLAVE
---
---PAN_MASTER
---
---PAN_SLAVE
---
---WIDTH_MASTER
---
---WIDTH_SLAVE
---
---MUTE_MASTER
---
---MUTE_SLAVE
---
---SOLO_MASTER
---
---SOLO_SLAVE
---
---RECARM_MASTER
---
---RECARM_SLAVE
---
---POLARITY_MASTER
---
---POLARITY_SLAVE
---
---AUTOMODE_MASTER
---
---AUTOMODE_SLAVE
---
---VOLUME_REVERSE
---
---PAN_REVERSE
---
---WIDTH_REVERSE
---
---NO_MASTER_WHEN_SLAVE
---
---VOLUME_VCA_SLAVE_ISPREFX
function reaper.GetSetTrackGroupMembership(tr, groupname, setmask, setvalue)
end


---Lua: integer reaper.GetSetTrackGroupMembershipHigh(MediaTrack tr, string groupname, integer setmask, integer setvalue)
---
---
---Gets or modifies the group membership for a track. Returns group state prior to call (each bit represents one of the high 32 group numbers). if setmask has bits set, those bits in setvalue will be applied to group. Group can be one of:
---
---VOLUME_MASTER
---
---VOLUME_SLAVE
---
---VOLUME_VCA_MASTER
---
---VOLUME_VCA_SLAVE
---
---PAN_MASTER
---
---PAN_SLAVE
---
---WIDTH_MASTER
---
---WIDTH_SLAVE
---
---MUTE_MASTER
---
---MUTE_SLAVE
---
---SOLO_MASTER
---
---SOLO_SLAVE
---
---RECARM_MASTER
---
---RECARM_SLAVE
---
---POLARITY_MASTER
---
---POLARITY_SLAVE
---
---AUTOMODE_MASTER
---
---AUTOMODE_SLAVE
---
---VOLUME_REVERSE
---
---PAN_REVERSE
---
---WIDTH_REVERSE
---
---NO_MASTER_WHEN_SLAVE
---
---VOLUME_VCA_SLAVE_ISPREFX
function reaper.GetSetTrackGroupMembershipHigh(tr, groupname, setmask, setvalue)
end


---Lua: boolean retval, string str = reaper.GetSetTrackState(MediaTrack track, string str)
---
---
---deprecated -- see SetTrackStateChunk
---, GetTrackStateChunk
function reaper.GetSetTrackState(track, str)
end


---Lua: boolean retval, string str = reaper.GetSetTrackState2(MediaTrack track, string str, boolean isundo)
---
---
---deprecated -- see SetTrackStateChunk
---, GetTrackStateChunk
function reaper.GetSetTrackState2(track, str, isundo)
end


---Lua: ReaProject reaper.GetSubProjectFromSource(PCM_source src)
function reaper.GetSubProjectFromSource(src)
end


---Lua: MediaItem_Take reaper.GetTake(MediaItem item, integer takeidx)
---
---
---get a take from an item by take count (zero-based)
function reaper.GetTake(item, takeidx)
end


---Lua: TrackEnvelope reaper.GetTakeEnvelope(MediaItem_Take take, integer envidx)
function reaper.GetTakeEnvelope(take, envidx)
end


---Lua: TrackEnvelope reaper.GetTakeEnvelopeByName(MediaItem_Take take, string envname)
function reaper.GetTakeEnvelopeByName(take, envname)
end


---Lua: string reaper.GetTakeName(MediaItem_Take take)
---
---
---returns NULL if the take is not valid
function reaper.GetTakeName(take)
end


---Lua: integer reaper.GetTakeNumStretchMarkers(MediaItem_Take take)
---
---
---Returns number of stretch markers in take
function reaper.GetTakeNumStretchMarkers(take)
end


---Lua: integer retval, number pos, optional number srcpos = reaper.GetTakeStretchMarker(MediaItem_Take take, integer idx)
---
---
---Gets information on a stretch marker, idx is 0..n. Returns false if stretch marker not valid. posOut will be set to position in item, srcposOutOptional will be set to source media position. Returns index. if input index is -1, next marker is found using position (or source position if position is -1). If position/source position are used to find marker position, their values are not updated.
function reaper.GetTakeStretchMarker(take, idx)
end


---Lua: number reaper.GetTakeStretchMarkerSlope(MediaItem_Take take, integer idx)
---
---
---See SetTakeStretchMarkerSlope
function reaper.GetTakeStretchMarkerSlope(take, idx)
end


---Lua: boolean retval, number fxindex, number parmidx = reaper.GetTCPFXParm(ReaProject project, MediaTrack track, integer index)
---
---
---Get information about a specific FX parameter knob (see CountTCPFXParms
---).
function reaper.GetTCPFXParm(project, track, index)
end


---Lua: boolean retval, number rate, number targetlen = reaper.GetTempoMatchPlayRate(PCM_source source, number srcscale, number position, number mult)
---
---
---finds the playrate and target length to insert this item stretched to a round power-of-2 number of bars, between 1/8 and 256
function reaper.GetTempoMatchPlayRate(source, srcscale, position, mult)
end


---Lua: boolean retval, number timepos, number measurepos, number beatpos, number bpm, number timesig_num, number timesig_denom, boolean lineartempo = reaper.GetTempoTimeSigMarker(ReaProject proj, integer ptidx)
---
---
---Get information about a tempo/time signature marker. See CountTempoTimeSigMarkers
---, SetTempoTimeSigMarker
---, AddTempoTimeSigMarker
---.
function reaper.GetTempoTimeSigMarker(proj, ptidx)
end


---Lua: integer reaper.GetToggleCommandState(integer command_id)
---
---
---See GetToggleCommandStateEx
---.
function reaper.GetToggleCommandState(command_id)
end


---Lua: integer reaper.GetToggleCommandStateEx(integer section_id, integer command_id)
---
---
---For the main action context, the MIDI editor, or the media explorer, returns the toggle state of the action. 0=off, 1=on, -1=NA because the action does not have on/off states. For the MIDI editor, the action state for the most recently focused window will be returned.
function reaper.GetToggleCommandStateEx(section_id, command_id)
end


---Lua: HWND reaper.GetTooltipWindow()
---
---
---gets a tooltip window,in case you want to ask it for font information. Can return NULL.
function reaper.GetTooltipWindow()
end


---Lua: MediaTrack reaper.GetTrack(ReaProject proj, integer trackidx)
---
---
---get a track from a project by track count (zero-based) (proj=0 for active project)
function reaper.GetTrack(proj, trackidx)
end


---Lua: integer reaper.GetTrackAutomationMode(MediaTrack tr)
---
---
---return the track mode, regardless of global override
function reaper.GetTrackAutomationMode(tr)
end


---Lua: integer reaper.GetTrackColor(MediaTrack track)
---
---
---Returns the track custom color as OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). Black is returned as 0x01000000, no color setting is returned as 0.
function reaper.GetTrackColor(track)
end


---Lua: integer reaper.GetTrackDepth(MediaTrack track)
function reaper.GetTrackDepth(track)
end


---Lua: TrackEnvelope reaper.GetTrackEnvelope(MediaTrack track, integer envidx)
function reaper.GetTrackEnvelope(track, envidx)
end


---Lua: TrackEnvelope reaper.GetTrackEnvelopeByChunkName(MediaTrack tr, string cfgchunkname)
---
---
---Gets a built-in track envelope by configuration chunk name, e.g. "<VOLENV".
function reaper.GetTrackEnvelopeByChunkName(tr, cfgchunkname)
end


---Lua: TrackEnvelope reaper.GetTrackEnvelopeByName(MediaTrack track, string envname)
function reaper.GetTrackEnvelopeByName(track, envname)
end


---Lua: string GUID = reaper.GetTrackGUID(MediaTrack tr)
function reaper.GetTrackGUID(tr)
end


---Lua: MediaItem reaper.GetTrackMediaItem(MediaTrack tr, integer itemidx)
function reaper.GetTrackMediaItem(tr, itemidx)
end


---Lua: boolean retval, string bufWant16384 = reaper.GetTrackMIDILyrics(MediaTrack track, integer flag, string bufWant16384)
---
---
---Get all MIDI lyrics on the track. Lyrics will be returned as one string with tabs between each word. flag&1: double tabs at the end of each measure and triple tabs when skipping measures, flag&2: each lyric is preceded by its beat position in the project (example with flag=2: "1.1.2\tLyric for measure 1 beat 2\t.1.1\tLyric for measure 2 beat 1	"). See SetTrackMIDILyrics
function reaper.GetTrackMIDILyrics(track, flag, bufWant16384)
end


---Lua: string reaper.GetTrackMIDINoteName(integer track, integer pitch, integer chan)
---
---
---see GetTrackMIDINoteNameEx
function reaper.GetTrackMIDINoteName(track, pitch, chan)
end


---Lua: string reaper.GetTrackMIDINoteNameEx(ReaProject proj, MediaTrack track, integer pitch, integer chan)
---
---
---Get note/CC name. pitch 128 for CC0 name, 129 for CC1 name, etc. See SetTrackMIDINoteNameEx
function reaper.GetTrackMIDINoteNameEx(proj, track, pitch, chan)
end


---Lua: number note_lo, number note_hi = reaper.GetTrackMIDINoteRange(ReaProject proj, MediaTrack track)
function reaper.GetTrackMIDINoteRange(proj, track)
end


---Lua: boolean retval, string buf = reaper.GetTrackName(MediaTrack track, string buf)
---
---
---Returns "MASTER" for master track, "Track N" if track has no name.
function reaper.GetTrackName(track, buf)
end


---Lua: integer reaper.GetTrackNumMediaItems(MediaTrack tr)
function reaper.GetTrackNumMediaItems(tr)
end


---Lua: integer reaper.GetTrackNumSends(MediaTrack tr, integer category)
---
---
---returns number of sends/receives/hardware outputs - category is <0 for receives, 0=sends, >0 for hardware outputs
function reaper.GetTrackNumSends(tr, category)
end


---Lua: boolean retval, string buf = reaper.GetTrackReceiveName(MediaTrack track, integer recv_index, string buf)
---
---
---See GetTrackSendName
---.
function reaper.GetTrackReceiveName(track, recv_index, buf)
end


---Lua: boolean retval, boolean mute = reaper.GetTrackReceiveUIMute(MediaTrack track, integer recv_index)
---
---
---See GetTrackSendUIMute
---.
function reaper.GetTrackReceiveUIMute(track, recv_index)
end


---Lua: boolean retval, number volume, number pan = reaper.GetTrackReceiveUIVolPan(MediaTrack track, integer recv_index)
---
---
---See GetTrackSendUIVolPan
---.
function reaper.GetTrackReceiveUIVolPan(track, recv_index)
end


---Lua: number reaper.GetTrackSendInfo_Value(MediaTrack tr, integer category, integer sendidx, string parmname)
---
---
---Get send/receive/hardware output numerical-value attributes.
---
---category is <0 for receives, 0=sends, >0 for hardware outputs
---
---parameter names:
---
---B_MUTE : returns bool *
---
---B_PHASE : returns bool *, true to flip phase
---
---B_MONO : returns bool *
---
---D_VOL : returns double *, 1.0 = +0dB etc
---
---D_PAN : returns double *, -1..+1
---
---D_PANLAW : returns double *,1.0=+0.0db, 0.5=-6dB, -1.0 = projdef etc
---
---I_SENDMODE : returns int *, 0=post-fader, 1=pre-fx, 2=post-fx (deprecated), 3=post-fx
---
---I_AUTOMODE : returns int * : automation mode (-1=use track automode, 0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
---
---I_SRCCHAN : returns int *, index,&1024=mono, -1 for none
---
---I_DSTCHAN : returns int *, index, &1024=mono, otherwise stereo pair, hwout:&512=rearoute
---
---I_MIDIFLAGS : returns int *, low 5 bits=source channel 0=all, 1-16, next 5 bits=dest channel, 0=orig, 1-16=chanP_DESTTRACK : read only, returns MediaTrack *, destination track, only applies for sends/recvs
---
---P_SRCTRACK : read only, returns MediaTrack *, source track, only applies for sends/recvs
---
---P_ENV : read only, returns TrackEnvelope *, setNewValue=<VOLENV, <PANENV, etc
---
---See CreateTrackSend
---, RemoveTrackSend
---, GetTrackNumSends
---.
function reaper.GetTrackSendInfo_Value(tr, category, sendidx, parmname)
end


---Lua: boolean retval, string buf = reaper.GetTrackSendName(MediaTrack track, integer send_index, string buf)
---
---
---send_idx>=0 for hw ouputs, >=nb_of_hw_ouputs for sends. See GetTrackReceiveName
---.
function reaper.GetTrackSendName(track, send_index, buf)
end


---Lua: boolean retval, boolean mute = reaper.GetTrackSendUIMute(MediaTrack track, integer send_index)
---
---
---send_idx>=0 for hw ouputs, >=nb_of_hw_ouputs for sends. See GetTrackReceiveUIMute
---.
function reaper.GetTrackSendUIMute(track, send_index)
end


---Lua: boolean retval, number volume, number pan = reaper.GetTrackSendUIVolPan(MediaTrack track, integer send_index)
---
---
---send_idx>=0 for hw ouputs, >=nb_of_hw_ouputs for sends. See GetTrackReceiveUIVolPan
---.
function reaper.GetTrackSendUIVolPan(track, send_index)
end


---Lua: string retval, number flags = reaper.GetTrackState(MediaTrack track)
---
---
---Gets track state, returns track name.
---
---flags will be set to:
---
---&1=folder
---
---&2=selected
---
---&4=has fx enabled
---
---&8=muted
---
---&16=soloed
---
---&32=SIP'd (with &16)
---
---&64=rec armed
---
---&128=rec monitoring on
---
---&256=rec monitoring auto
---
---&512=hide from TCP
---
---&1024=hide from MCP
function reaper.GetTrackState(track)
end


---Lua: boolean retval, string str = reaper.GetTrackStateChunk(MediaTrack track, string str, boolean isundo)
---
---
---Gets the RPPXML state of a track, returns true if successful. Undo flag is a performance/caching hint.
function reaper.GetTrackStateChunk(track, str, isundo)
end


---Lua: boolean retval, boolean mute = reaper.GetTrackUIMute(MediaTrack track)
function reaper.GetTrackUIMute(track)
end


---Lua: boolean retval, number pan1, number pan2, number panmode = reaper.GetTrackUIPan(MediaTrack track)
function reaper.GetTrackUIPan(track)
end


---Lua: boolean retval, number volume, number pan = reaper.GetTrackUIVolPan(MediaTrack track)
function reaper.GetTrackUIVolPan(track)
end


---Lua: optional number audio_xrun, optional number media_xrun, optional number curtime = reaper.GetUnderrunTime()
---
---
---retrieves the last timestamps of audio xrun (yellow-flash, if available), media xrun (red-flash), and the current time stamp (all milliseconds)
function reaper.GetUnderrunTime()
end


---Lua: boolean retval, string filenameNeed4096 = reaper.GetUserFileNameForRead(string filenameNeed4096, string title, string defext)
---
---
---returns true if the user selected a valid file, false if the user canceled the dialog
function reaper.GetUserFileNameForRead(filenameNeed4096, title, defext)
end


---Lua: boolean retval, string retvals_csv = reaper.GetUserInputs(string title, integer num_inputs, string captions_csv, string retvals_csv)
---
---
---Get values from the user.
---
---If a caption begins with *, for example "*password", the edit field will not display the input text.
---
---Maximum fields is 16. Values are returned as a comma-separated string. Returns false if the user canceled the dialog. To increase text field width, add an extra caption field, and specify extrawidth=xyz
function reaper.GetUserInputs(title, num_inputs, captions_csv, retvals_csv)
end


---Lua: reaper.GoToMarker(ReaProject proj, integer marker_index, boolean use_timeline_order)
---
---
---Go to marker. If use_timeline_order==true, marker_index 1 refers to the first marker on the timeline.  If use_timeline_order==false, marker_index 1 refers to the first marker with the user-editable index of 1.
function reaper.GoToMarker(proj, marker_index, use_timeline_order)
end


---Lua: reaper.GoToRegion(ReaProject proj, integer region_index, boolean use_timeline_order)
---
---
---Seek to region after current region finishes playing (smooth seek). If use_timeline_order==true, region_index 1 refers to the first region on the timeline.  If use_timeline_order==false, region_index 1 refers to the first region with the user-editable index of 1.
function reaper.GoToRegion(proj, region_index, use_timeline_order)
end


---Lua: integer retval, number color = reaper.GR_SelectColor(HWND hwnd)
---
---
---Runs the system color chooser dialog.  Returns 0 if the user cancels the dialog.
function reaper.GR_SelectColor(hwnd)
end


---Lua: integer reaper.GSC_mainwnd(integer t)
---
---
---this is just like win32 GetSysColor() but can have overrides.
function reaper.GSC_mainwnd(t)
end


---Lua: string destNeed64 = reaper.guidToString(string gGUID, string destNeed64)
---
---
---dest should be at least 64 chars long to be safe
function reaper.guidToString(gGUID, destNeed64)
end


---Lua: boolean reaper.HasExtState(string section, string key)
---
---
---Returns true if there exists an extended state value for a specific section and key. See SetExtState
---, GetExtState
---, DeleteExtState
---.
function reaper.HasExtState(section, key)
end


---Lua: string reaper.HasTrackMIDIPrograms(integer track)
---
---
---returns name of track plugin that is supplying MIDI programs,or NULL if there is none
function reaper.HasTrackMIDIPrograms(track)
end


---Lua: string reaper.HasTrackMIDIProgramsEx(ReaProject proj, MediaTrack track)
---
---
---returns name of track plugin that is supplying MIDI programs,or NULL if there is none
function reaper.HasTrackMIDIProgramsEx(proj, track)
end


---Lua: reaper.Help_Set(string helpstring, boolean is_temporary_help)
function reaper.Help_Set(helpstring, is_temporary_help)
end


---Lua: string out = reaper.image_resolve_fn(string in, string out)
function reaper.image_resolve_fn(In, out)
end


---Lua: integer reaper.InsertAutomationItem(TrackEnvelope env, integer pool_id, number position, number length)
---
---
---Insert a new automation item. pool_id < 0 collects existing envelope points into the automation item; otherwise, the automation item will be a new instance of an existing pool. Returns the index of the item, suitable for passing to other automation item API functions. See GetSetAutomationItemInfo
---.
function reaper.InsertAutomationItem(env, pool_id, position, length)
end


---Lua: boolean reaper.InsertEnvelopePoint(TrackEnvelope envelope, number time, number value, integer shape, number tension, boolean selected, optional boolean noSortIn)
---
---
---Insert an envelope point. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done. See GetEnvelopePoint
---, SetEnvelopePoint
---, GetEnvelopeScalingMode
---.
function reaper.InsertEnvelopePoint(envelope, time, value, shape, tension, selected, noSortIn)
end


---Lua: boolean reaper.InsertEnvelopePointEx(TrackEnvelope envelope, integer autoitem_idx, number time, number value, integer shape, number tension, boolean selected, optional boolean noSortIn)
---
---
---Insert an envelope point. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done.  autoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePoint
---, SetEnvelopePoint
---, GetEnvelopeScalingMode
---.
function reaper.InsertEnvelopePointEx(envelope, autoitem_idx, time, value, shape, tension, selected, noSortIn)
end


---Lua: integer reaper.InsertMedia(string file, integer mode)
---
---
---mode: 0=add to current track, 1=add new track, 3=add to selected items as takes, &4=stretch/loop to fit time sel, &8=try to match tempo 1x, &16=try to match tempo 0.5x, &32=try to match tempo 2x, &64=don't preserve pitch when matching tempo, &128=no loop/section if startpct/endpct set, &256=force loop regardless of global preference for looping imported items. &512=use high word as absolute track index if mode&3==0.
function reaper.InsertMedia(file, mode)
end


---Lua: integer reaper.InsertMediaSection(string file, integer mode, number startpct, number endpct, number pitchshift)
function reaper.InsertMediaSection(file, mode, startpct, endpct, pitchshift)
end


---Lua: reaper.InsertTrackAtIndex(integer idx, boolean wantDefaults)
---
---
---inserts a track at idx,of course this will be clamped to 0..GetNumTracks(). wantDefaults=TRUE for default envelopes/FX,otherwise no enabled fx/env
function reaper.InsertTrackAtIndex(idx, wantDefaults)
end


---Lua: boolean reaper.IsMediaExtension(string ext, boolean wantOthers)
---
---
---Tests a file extension (i.e. "wav" or "mid") to see if it's a media extension.
---
---If wantOthers is set, then "RPP", "TXT" and other project-type formats will also pass.
function reaper.IsMediaExtension(ext, wantOthers)
end


---Lua: boolean reaper.IsMediaItemSelected(MediaItem item)
function reaper.IsMediaItemSelected(item)
end


---Lua: integer reaper.IsProjectDirty(ReaProject proj)
---
---
---Is the project dirty (needing save)? Always returns 0 if 'undo/prompt to save' is disabled in preferences.
function reaper.IsProjectDirty(proj)
end


---Lua: boolean reaper.IsTrackSelected(MediaTrack track)
function reaper.IsTrackSelected(track)
end


---Lua: boolean reaper.IsTrackVisible(MediaTrack track, boolean mixer)
---
---
---If mixer==true, returns true if the track is visible in the mixer.  If mixer==false, returns true if the track is visible in the track control panel.
function reaper.IsTrackVisible(track, mixer)
end


---Lua: joystick_device reaper.joystick_create(string guidGUID)
---
---
---creates a joystick device
function reaper.joystick_create(guidGUID)
end


---Lua: reaper.joystick_destroy(joystick_device device)
---
---
---destroys a joystick device
function reaper.joystick_destroy(device)
end


---Lua: string retval, optional string namestr = reaper.joystick_enum(integer index)
---
---
---enumerates installed devices, returns GUID as a string
function reaper.joystick_enum(index)
end


---Lua: number reaper.joystick_getaxis(joystick_device dev, integer axis)
---
---
---returns axis value (-1..1)
function reaper.joystick_getaxis(dev, axis)
end


---Lua: integer reaper.joystick_getbuttonmask(joystick_device dev)
---
---
---returns button pressed mask, 1=first button, 2=second...
function reaper.joystick_getbuttonmask(dev)
end


---Lua: integer retval, optional number axes, optional number povs = reaper.joystick_getinfo(joystick_device dev)
---
---
---returns button count
function reaper.joystick_getinfo(dev)
end


---Lua: number reaper.joystick_getpov(joystick_device dev, integer pov)
---
---
---returns POV value (usually 0..655.35, or 655.35 on error)
function reaper.joystick_getpov(dev, pov)
end


---Lua: boolean reaper.joystick_update(joystick_device dev)
---
---
---Updates joystick state from hardware, returns true if successful (joystick_get* will not be valid until joystick_update() is called successfully)
function reaper.joystick_update(dev)
end


---Lua: boolean retval, number pX1, number pY1, number pX2, number pY2 = reaper.LICE_ClipLine(number pX1, number pY1, number pX2, number pY2, integer xLo, integer yLo, integer xHi, integer yHi)
---
---
---Returns false if the line is entirely offscreen.
function reaper.LICE_ClipLine(pX1, pY1, pX2, pY2, xLo, yLo, xHi, yHi)
end


---Lua: boolean reaper.Loop_OnArrow(ReaProject project, integer direction)
---
---
---Move the loop selection left or right. Returns true if snap is enabled.
function reaper.Loop_OnArrow(project, direction)
end


---Lua: reaper.Main_OnCommand(integer command, integer flag)
---
---
---See Main_OnCommandEx
---.
function reaper.Main_OnCommand(command, flag)
end


---Lua: reaper.Main_OnCommandEx(integer command, integer flag, ReaProject proj)
---
---
---Performs an action belonging to the main action section. To perform non-native actions (ReaScripts, custom or extension plugins' actions) safely, see NamedCommandLookup
---().
function reaper.Main_OnCommandEx(command, flag, proj)
end


---Lua: reaper.Main_openProject(string name)
---
---
---opens a project. will prompt the user to save, etc.
---
---if you pass a .RTrackTemplate file then it adds that to the project instead.
function reaper.Main_openProject(name)
end


---Lua: reaper.Main_SaveProject(ReaProject proj, boolean forceSaveAsIn)
---
---
---Save the project.
function reaper.Main_SaveProject(proj, forceSaveAsIn)
end


---Lua: reaper.Main_UpdateLoopInfo(integer ignoremask)
function reaper.Main_UpdateLoopInfo(ignoremask)
end


---Lua: reaper.MarkProjectDirty(ReaProject proj)
---
---
---Marks project as dirty (needing save) if 'undo/prompt to save' is enabled in preferences.
function reaper.MarkProjectDirty(proj)
end


---Lua: reaper.MarkTrackItemsDirty(MediaTrack track, MediaItem item)
---
---
---If track is supplied, item is ignored
function reaper.MarkTrackItemsDirty(track, item)
end


---Lua: number reaper.Master_GetPlayRate(ReaProject project)
function reaper.Master_GetPlayRate(project)
end


---Lua: number reaper.Master_GetPlayRateAtTime(number time_s, ReaProject proj)
function reaper.Master_GetPlayRateAtTime(time_s, proj)
end


---Lua: number reaper.Master_GetTempo()
function reaper.Master_GetTempo()
end


---Lua: number reaper.Master_NormalizePlayRate(number playrate, boolean isnormalized)
---
---
---Convert play rate to/from a value between 0 and 1, representing the position on the project playrate slider.
function reaper.Master_NormalizePlayRate(playrate, isnormalized)
end


---Lua: number reaper.Master_NormalizeTempo(number bpm, boolean isnormalized)
---
---
---Convert the tempo to/from a value between 0 and 1, representing bpm in the range of 40-296 bpm.
function reaper.Master_NormalizeTempo(bpm, isnormalized)
end


---Lua: integer reaper.MB(string msg, string title, integer type)
---
---
---type 0=OK,1=OKCANCEL,2=ABORTRETRYIGNORE,3=YESNOCANCEL,4=YESNO,5=RETRYCANCEL : ret 1=OK,2=CANCEL,3=ABORT,4=RETRY,5=IGNORE,6=YES,7=NO
function reaper.MB(msg, title, type)
end


---Lua: integer reaper.MediaItemDescendsFromTrack(MediaItem item, MediaTrack track)
---
---
---Returns 1 if the track holds the item, 2 if the track is a folder containing the track that holds the item, etc.
function reaper.MediaItemDescendsFromTrack(item, track)
end


---Lua: integer retval, number notecnt, number ccevtcnt, number textsyxevtcnt = reaper.MIDI_CountEvts(MediaItem_Take take)
---
---
---Count the number of notes, CC events, and text/sysex events in a given MIDI item.
function reaper.MIDI_CountEvts(take)
end


---Lua: boolean reaper.MIDI_DeleteCC(MediaItem_Take take, integer ccidx)
---
---
---Delete a MIDI CC event.
function reaper.MIDI_DeleteCC(take, ccidx)
end


---Lua: boolean reaper.MIDI_DeleteEvt(MediaItem_Take take, integer evtidx)
---
---
---Delete a MIDI event.
function reaper.MIDI_DeleteEvt(take, evtidx)
end


---Lua: boolean reaper.MIDI_DeleteNote(MediaItem_Take take, integer noteidx)
---
---
---Delete a MIDI note.
function reaper.MIDI_DeleteNote(take, noteidx)
end


---Lua: boolean reaper.MIDI_DeleteTextSysexEvt(MediaItem_Take take, integer textsyxevtidx)
---
---
---Delete a MIDI text or sysex event.
function reaper.MIDI_DeleteTextSysexEvt(take, textsyxevtidx)
end


---Lua: integer reaper.MIDI_EnumSelCC(MediaItem_Take take, integer ccidx)
---
---
---Returns the index of the next selected MIDI CC event after ccidx (-1 if there are no more selected events).
function reaper.MIDI_EnumSelCC(take, ccidx)
end


---Lua: integer reaper.MIDI_EnumSelEvts(MediaItem_Take take, integer evtidx)
---
---
---Returns the index of the next selected MIDI event after evtidx (-1 if there are no more selected events).
function reaper.MIDI_EnumSelEvts(take, evtidx)
end


---Lua: integer reaper.MIDI_EnumSelNotes(MediaItem_Take take, integer noteidx)
---
---
---Returns the index of the next selected MIDI note after noteidx (-1 if there are no more selected events).
function reaper.MIDI_EnumSelNotes(take, noteidx)
end


---Lua: integer reaper.MIDI_EnumSelTextSysexEvts(MediaItem_Take take, integer textsyxidx)
---
---
---Returns the index of the next selected MIDI text/sysex event after textsyxidx (-1 if there are no more selected events).
function reaper.MIDI_EnumSelTextSysexEvts(take, textsyxidx)
end


---Lua: boolean retval, string buf = reaper.MIDI_GetAllEvts(MediaItem_Take take, string buf)
---
---
---Get all MIDI data. MIDI buffer is returned as a list of { int offset, char flag, int msglen, unsigned char msg[] }. offset: MIDI ticks from previous event, flag: &1=selected &2=muted, msglen: byte length of msg (usually 3), msg: the MIDI message. For tick intervals longer than a 32 bit word can represent, zero-length meta events may be placed between valid events. See MIDI_SetAllEvts
---.
function reaper.MIDI_GetAllEvts(take, buf)
end


---Lua: boolean retval, boolean selected, boolean muted, number ppqpos, number chanmsg, number chan, number msg2, number msg3 = reaper.MIDI_GetCC(MediaItem_Take take, integer ccidx)
---
---
---Get MIDI CC event properties.
function reaper.MIDI_GetCC(take, ccidx)
end


---Lua: boolean retval, boolean selected, boolean muted, number ppqpos, string msg = reaper.MIDI_GetEvt(MediaItem_Take take, integer evtidx, boolean selected, boolean muted, number ppqpos, string msg)
---
---
---Get MIDI event properties.
function reaper.MIDI_GetEvt(take, evtidx, selected, muted, ppqpos, msg)
end


---Lua: number retval, optional number swing, optional number noteLen = reaper.MIDI_GetGrid(MediaItem_Take take)
---
---
---Returns the most recent MIDI editor grid size for this MIDI take, in QN. Swing is between 0 and 1. Note length is 0 if it follows the grid size.
function reaper.MIDI_GetGrid(take)
end


---Lua: boolean retval, string hash = reaper.MIDI_GetHash(MediaItem_Take take, boolean notesonly, string hash)
---
---
---Get a string that only changes when the MIDI data changes. If notesonly==true, then the string changes only when the MIDI notes change. See MIDI_GetTrackHash
function reaper.MIDI_GetHash(take, notesonly, hash)
end


---Lua: boolean retval, boolean selected, boolean muted, number startppqpos, number endppqpos, number chan, number pitch, number vel = reaper.MIDI_GetNote(MediaItem_Take take, integer noteidx)
---
---
---Get MIDI note properties.
function reaper.MIDI_GetNote(take, noteidx)
end


---Lua: number reaper.MIDI_GetPPQPos_EndOfMeasure(MediaItem_Take take, number ppqpos)
---
---
---Returns the MIDI tick (ppq) position corresponding to the end of the measure.
function reaper.MIDI_GetPPQPos_EndOfMeasure(take, ppqpos)
end


---Lua: number reaper.MIDI_GetPPQPos_StartOfMeasure(MediaItem_Take take, number ppqpos)
---
---
---Returns the MIDI tick (ppq) position corresponding to the start of the measure.
function reaper.MIDI_GetPPQPos_StartOfMeasure(take, ppqpos)
end


---Lua: number reaper.MIDI_GetPPQPosFromProjQN(MediaItem_Take take, number projqn)
---
---
---Returns the MIDI tick (ppq) position corresponding to a specific project time in quarter notes.
function reaper.MIDI_GetPPQPosFromProjQN(take, projqn)
end


---Lua: number reaper.MIDI_GetPPQPosFromProjTime(MediaItem_Take take, number projtime)
---
---
---Returns the MIDI tick (ppq) position corresponding to a specific project time in seconds.
function reaper.MIDI_GetPPQPosFromProjTime(take, projtime)
end


---Lua: number reaper.MIDI_GetProjQNFromPPQPos(MediaItem_Take take, number ppqpos)
---
---
---Returns the project time in quarter notes corresponding to a specific MIDI tick (ppq) position.
function reaper.MIDI_GetProjQNFromPPQPos(take, ppqpos)
end


---Lua: number reaper.MIDI_GetProjTimeFromPPQPos(MediaItem_Take take, number ppqpos)
---
---
---Returns the project time in seconds corresponding to a specific MIDI tick (ppq) position.
function reaper.MIDI_GetProjTimeFromPPQPos(take, ppqpos)
end


---Lua: boolean retval, number root, number scale, string name = reaper.MIDI_GetScale(MediaItem_Take take, number root, number scale, string name)
---
---
---Get the active scale in the media source, if any. root 0=C, 1=C#, etc. scale &0x1=root, &0x2=minor 2nd, &0x4=major 2nd, &0x8=minor 3rd, &0xF=fourth, etc.
function reaper.MIDI_GetScale(take, root, scale, name)
end


---Lua: boolean retval, optional boolean selected, optional boolean muted, optional number ppqpos, optional number type, optional string msg = reaper.MIDI_GetTextSysexEvt(MediaItem_Take take, integer textsyxevtidx, optional boolean selected, optional boolean muted, optional number ppqpos, optional number type, optional string msg)
---
---
---Get MIDI meta-event properties. Allowable types are -1:sysex (msg should not include bounding F0..F7), 1-7:MIDI text event types.
function reaper.MIDI_GetTextSysexEvt(take, textsyxevtidx, selected, muted, ppqpos, type, msg)
end


---Lua: boolean retval, string hash = reaper.MIDI_GetTrackHash(MediaTrack track, boolean notesonly, string hash)
---
---
---Get a string that only changes when the MIDI data changes. If notesonly==true, then the string changes only when the MIDI notes change. See MIDI_GetHash
function reaper.MIDI_GetTrackHash(track, notesonly, hash)
end


---Lua: boolean reaper.MIDI_InsertCC(MediaItem_Take take, boolean selected, boolean muted, number ppqpos, integer chanmsg, integer chan, integer msg2, integer msg3)
---
---
---Insert a new MIDI CC event.
function reaper.MIDI_InsertCC(take, selected, muted, ppqpos, chanmsg, chan, msg2, msg3)
end


---Lua: boolean reaper.MIDI_InsertEvt(MediaItem_Take take, boolean selected, boolean muted, number ppqpos, string bytestr)
---
---
---Insert a new MIDI event.
function reaper.MIDI_InsertEvt(take, selected, muted, ppqpos, bytestr)
end


---Lua: boolean reaper.MIDI_InsertNote(MediaItem_Take take, boolean selected, boolean muted, number startppqpos, number endppqpos, integer chan, integer pitch, integer vel, optional boolean noSortIn)
---
---
---Insert a new MIDI note. Set noSort if inserting multiple events, then call MIDI_Sort when done.
function reaper.MIDI_InsertNote(take, selected, muted, startppqpos, endppqpos, chan, pitch, vel, noSortIn)
end


---Lua: boolean reaper.MIDI_InsertTextSysexEvt(MediaItem_Take take, boolean selected, boolean muted, number ppqpos, integer type, string bytestr)
---
---
---Insert a new MIDI text or sysex event. Allowable types are -1:sysex (msg should not include bounding F0..F7), 1-7:MIDI text event types.
function reaper.MIDI_InsertTextSysexEvt(take, selected, muted, ppqpos, type, bytestr)
end


---Lua: reaper.midi_reinit()
---
---
---Reset all MIDI devices
function reaper.midi_reinit()
end


---Lua: reaper.MIDI_SelectAll(MediaItem_Take take, boolean select)
---
---
---Select or deselect all MIDI content.
function reaper.MIDI_SelectAll(take, select)
end


---Lua: boolean reaper.MIDI_SetAllEvts(MediaItem_Take take, string buf)
---
---
---Set all MIDI data. MIDI buffer is passed in as a list of { int offset, char flag, int msglen, unsigned char msg[] }. offset: MIDI ticks from previous event, flag: &1=selected &2=muted, msglen: byte length of msg (usually 3), msg: the MIDI message. For tick intervals longer than a 32 bit word can represent, zero-length meta events may be placed between valid events. See MIDI_GetAllEvts
---.
function reaper.MIDI_SetAllEvts(take, buf)
end


---Lua: boolean reaper.MIDI_SetCC(MediaItem_Take take, integer ccidx, optional boolean selectedIn, optional boolean mutedIn, optional number ppqposIn, optional number chanmsgIn, optional number chanIn, optional number msg2In, optional number msg3In, optional boolean noSortIn)
---
---
---Set MIDI CC event properties. Properties passed as NULL will not be set. set noSort if setting multiple events, then call MIDI_Sort when done.
function reaper.MIDI_SetCC(take, ccidx, selectedIn, mutedIn, ppqposIn, chanmsgIn, chanIn, msg2In, msg3In, noSortIn)
end


---Lua: boolean reaper.MIDI_SetEvt(MediaItem_Take take, integer evtidx, optional boolean selectedIn, optional boolean mutedIn, optional number ppqposIn, optional string msg, optional boolean noSortIn)
---
---
---Set MIDI event properties. Properties passed as NULL will not be set.  set noSort if setting multiple events, then call MIDI_Sort when done.
function reaper.MIDI_SetEvt(take, evtidx, selectedIn, mutedIn, ppqposIn, msg, noSortIn)
end


---Lua: boolean reaper.MIDI_SetItemExtents(MediaItem item, number startQN, number endQN)
---
---
---Set the start/end positions of a media item that contains a MIDI take.
function reaper.MIDI_SetItemExtents(item, startQN, endQN)
end


---Lua: boolean reaper.MIDI_SetNote(MediaItem_Take take, integer noteidx, optional boolean selectedIn, optional boolean mutedIn, optional number startppqposIn, optional number endppqposIn, optional number chanIn, optional number pitchIn, optional number velIn, optional boolean noSortIn)
---
---
---Set MIDI note properties. Properties passed as NULL (or negative values) will not be set. Set noSort if setting multiple events, then call MIDI_Sort when done. Setting multiple note start positions at once is done more safely by deleting and re-inserting the notes.
function reaper.MIDI_SetNote(take, noteidx, selectedIn, mutedIn, startppqposIn, endppqposIn, chanIn, pitchIn, velIn, noSortIn)
end


---Lua: boolean reaper.MIDI_SetTextSysexEvt(MediaItem_Take take, integer textsyxevtidx, optional boolean selectedIn, optional boolean mutedIn, optional number ppqposIn, optional number typeIn, optional string msg, optional boolean noSortIn)
---
---
---Set MIDI text or sysex event properties. Properties passed as NULL will not be set. Allowable types are -1:sysex (msg should not include bounding F0..F7), 1-7:MIDI text event types. set noSort if setting multiple events, then call MIDI_Sort when done.
function reaper.MIDI_SetTextSysexEvt(take, textsyxevtidx, selectedIn, mutedIn, ppqposIn, typeIn, msg, noSortIn)
end


---Lua: reaper.MIDI_Sort(MediaItem_Take take)
---
---
---Sort MIDI events after multiple calls to MIDI_SetNote, MIDI_SetCC, etc.
function reaper.MIDI_Sort(take)
end


---Lua: HWND reaper.MIDIEditor_GetActive()
---
---
---get a pointer to the focused MIDI editor window
---
---see MIDIEditor_GetMode
---, MIDIEditor_OnCommand
function reaper.MIDIEditor_GetActive()
end


---Lua: integer reaper.MIDIEditor_GetMode(HWND midieditor)
---
---
---get the mode of a MIDI editor (0=piano roll, 1=event list, -1=invalid editor)
---
---see MIDIEditor_GetActive
---, MIDIEditor_OnCommand
function reaper.MIDIEditor_GetMode(midieditor)
end


---Lua: integer reaper.MIDIEditor_GetSetting_int(HWND midieditor, string setting_desc)
---
---
---Get settings from a MIDI editor. setting_desc can be:
---
---snap_enabled: returns 0 or 1
---
---active_note_row: returns 0-127
---
---last_clicked_cc_lane: returns 0-127=CC, 0x100|(0-31)=14-bit CC, 0x200=velocity, 0x201=pitch, 0x202=program, 0x203=channel pressure, 0x204=bank/program select, 0x205=text, 0x206=sysex, 0x207=off velocity
---
---default_note_vel: returns 0-127
---
---default_note_chan: returns 0-15
---
---default_note_len: returns default length in MIDI ticks
---
---scale_enabled: returns 0-1
---
---scale_root: returns 0-12 (0=C)
---
---if setting_desc is unsupported, the function returns -1.
---
---See MIDIEditor_GetActive
---, MIDIEditor_GetSetting_str
function reaper.MIDIEditor_GetSetting_int(midieditor, setting_desc)
end


---Lua: boolean retval, string buf = reaper.MIDIEditor_GetSetting_str(HWND midieditor, string setting_desc, string buf)
---
---
---Get settings from a MIDI editor. setting_desc can be:
---
---last_clicked_cc_lane: returns text description ("velocity", "pitch", etc)
---
---scale: returns the scale record, for example "102034050607" for a major scale
---
---if setting_desc is unsupported, the function returns false.
---
---See MIDIEditor_GetActive
---, MIDIEditor_GetSetting_int
function reaper.MIDIEditor_GetSetting_str(midieditor, setting_desc, buf)
end


---Lua: MediaItem_Take reaper.MIDIEditor_GetTake(HWND midieditor)
---
---
---get the take that is currently being edited in this MIDI editor
function reaper.MIDIEditor_GetTake(midieditor)
end


---Lua: boolean reaper.MIDIEditor_LastFocused_OnCommand(integer command_id, boolean islistviewcommand)
---
---
---Send an action command to the last focused MIDI editor. Returns false if there is no MIDI editor open, or if the view mode (piano roll or event list) does not match the input.
---
---see MIDIEditor_OnCommand
function reaper.MIDIEditor_LastFocused_OnCommand(command_id, islistviewcommand)
end


---Lua: boolean reaper.MIDIEditor_OnCommand(HWND midieditor, integer command_id)
---
---
---Send an action command to a MIDI editor. Returns false if the supplied MIDI editor pointer is not valid (not an open MIDI editor).
---
---see MIDIEditor_GetActive
---, MIDIEditor_LastFocused_OnCommand
function reaper.MIDIEditor_OnCommand(midieditor, command_id)
end


---Lua: string strNeed64 = reaper.mkpanstr(string strNeed64, number pan)
function reaper.mkpanstr(strNeed64, pan)
end


---Lua: string strNeed64 = reaper.mkvolpanstr(string strNeed64, number vol, number pan)
function reaper.mkvolpanstr(strNeed64, vol, pan)
end


---Lua: string strNeed64 = reaper.mkvolstr(string strNeed64, number vol)
function reaper.mkvolstr(strNeed64, vol)
end


---Lua: reaper.MoveEditCursor(number adjamt, boolean dosel)
function reaper.MoveEditCursor(adjamt, dosel)
end


---Lua: boolean reaper.MoveMediaItemToTrack(MediaItem item, MediaTrack desttr)
---
---
---returns TRUE if move succeeded
function reaper.MoveMediaItemToTrack(item, desttr)
end


---Lua: reaper.MuteAllTracks(boolean mute)
function reaper.MuteAllTracks(mute)
end


---Lua: reaper.my_getViewport(numberr.left, numberr.top, numberr.right, numberr.bot, number sr.left, number sr.top, number sr.right, number sr.bot, boolean wantWorkArea)
function reaper.my_getViewport(numberr_left, numberr_top, numberr_right, numberr_bot, sr_left, sr_top, sr_right, sr_bot, wantWorkArea)
end


---Lua: integer reaper.NamedCommandLookup(string command_name)
---
---
---Get the command ID number for named command that was registered by an extension such as "_SWS_ABOUT" or "_113088d11ae641c193a2b7ede3041ad5" for a ReaScript or a custom action.
function reaper.NamedCommandLookup(command_name)
end


---Lua: reaper.OnPauseButton()
---
---
---direct way to simulate pause button hit
function reaper.OnPauseButton()
end


---Lua: reaper.OnPauseButtonEx(ReaProject proj)
---
---
---direct way to simulate pause button hit
function reaper.OnPauseButtonEx(proj)
end


---Lua: reaper.OnPlayButton()
---
---
---direct way to simulate play button hit
function reaper.OnPlayButton()
end


---Lua: reaper.OnPlayButtonEx(ReaProject proj)
---
---
---direct way to simulate play button hit
function reaper.OnPlayButtonEx(proj)
end


---Lua: reaper.OnStopButton()
---
---
---direct way to simulate stop button hit
function reaper.OnStopButton()
end


---Lua: reaper.OnStopButtonEx(ReaProject proj)
---
---
---direct way to simulate stop button hit
function reaper.OnStopButtonEx(proj)
end


---Lua: boolean reaper.OpenColorThemeFile(string fn)
function reaper.OpenColorThemeFile(fn)
end


---Lua: HWND reaper.OpenMediaExplorer(string mediafn, boolean play)
---
---
---Opens mediafn in the Media Explorer, play=true will play the file immediately (or toggle playback if mediafn was already open), =false will just select it.
function reaper.OpenMediaExplorer(mediafn, play)
end


---Lua: reaper.OscLocalMessageToHost(string message, optional number valueIn)
---
---
---Send an OSC message directly to REAPER. The value argument may be NULL. The message will be matched against the default OSC patterns. Only supported if control surface support was enabled when installing REAPER.
function reaper.OscLocalMessageToHost(message, valueIn)
end


---Lua: number reaper.parse_timestr(string buf)
---
---
---Parse hh:mm:ss.sss time string, return time in seconds (or 0.0 on error). See parse_timestr_pos
---, parse_timestr_len
---.
function reaper.parse_timestr(buf)
end


---Lua: number reaper.parse_timestr_len(string buf, number offset, integer modeoverride)
---
---
---time formatting mode overrides: -1=proj default.
---
---0=time
---
---1=measures.beats + time
---
---2=measures.beats
---
---3=seconds
---
---4=samples
---
---5=h:m:s:f
function reaper.parse_timestr_len(buf, offset, modeoverride)
end


---Lua: number reaper.parse_timestr_pos(string buf, integer modeoverride)
---
---
---Parse time string, time formatting mode overrides: -1=proj default.
---
---0=time
---
---1=measures.beats + time
---
---2=measures.beats
---
---3=seconds
---
---4=samples
---
---5=h:m:s:f
function reaper.parse_timestr_pos(buf, modeoverride)
end


---Lua: number reaper.parsepanstr(string str)
function reaper.parsepanstr(str)
end


---Lua: integer retval, string descstr = reaper.PCM_Sink_Enum(integer idx)
function reaper.PCM_Sink_Enum(idx)
end


---Lua: string reaper.PCM_Sink_GetExtension(string data)
function reaper.PCM_Sink_GetExtension(data)
end


---Lua: HWND reaper.PCM_Sink_ShowConfig(string cfg, HWND hwndParent)
function reaper.PCM_Sink_ShowConfig(cfg, hwndParent)
end


---Lua: PCM_source reaper.PCM_Source_CreateFromFile(string filename)
---
---
---See PCM_Source_CreateFromFileEx
---.
function reaper.PCM_Source_CreateFromFile(filename)
end


---Lua: PCM_source reaper.PCM_Source_CreateFromFileEx(string filename, boolean forcenoMidiImp)
---
---
---Create a PCM_source from filename, and override pref of MIDI files being imported as in-project MIDI events.
function reaper.PCM_Source_CreateFromFileEx(filename, forcenoMidiImp)
end


---Lua: PCM_source reaper.PCM_Source_CreateFromType(string sourcetype)
---
---
---Create a PCM_source from a "type" (use this if you're going to load its state via LoadState/ProjectStateContext).
---
---Valid types include "WAVE", "MIDI", or whatever plug-ins define as well.
function reaper.PCM_Source_CreateFromType(sourcetype)
end


---Lua: reaper.PCM_Source_Destroy(PCM_source src)
---
---
---Deletes a PCM_source -- be sure that you remove any project reference before deleting a source
function reaper.PCM_Source_Destroy(src)
end


---Lua: integer reaper.PCM_Source_GetPeaks(PCM_source src, number peakrate, number starttime, integer numchannels, integer numsamplesperchannel, integer want_extra_type, reaper.array buf)
---
---
---Gets block of peak samples to buf. Note that the peak samples are interleaved, but in two or three blocks (maximums, then minimums, then extra). Return value has 20 bits of returned sample count, then 4 bits of output_mode (0xf00000), then a bit to signify whether extra_type was available (0x1000000). extra_type can be 115 ('s') for spectral information, which will return peak samples as integers with the low 15 bits frequency, next 14 bits tonality.
function reaper.PCM_Source_GetPeaks(src, peakrate, starttime, numchannels, numsamplesperchannel, want_extra_type, buf)
end


---Lua: boolean retval, number offs, number len, boolean rev = reaper.PCM_Source_GetSectionInfo(PCM_source src)
---
---
---If a section/reverse block, retrieves offset/len/reverse. return true if success
function reaper.PCM_Source_GetSectionInfo(src)
end


---Lua: reaper.PluginWantsAlwaysRunFx(integer amt)
function reaper.PluginWantsAlwaysRunFx(amt)
end


---Lua: reaper.PreventUIRefresh(integer prevent_count)
---
---
---adds prevent_count to the UI refresh prevention state; always add then remove the same amount, or major disfunction will occur
function reaper.PreventUIRefresh(prevent_count)
end


---Lua: reaper.ReaScriptError(string errmsg)
---
---
---Causes REAPER to display the error message after the current ReaScript finishes.
function reaper.ReaScriptError(errmsg)
end


---Lua: integer reaper.RecursiveCreateDirectory(string path, integer ignored)
---
---
---returns positive value on success, 0 on failure.
function reaper.RecursiveCreateDirectory(path, ignored)
end


---Lua: reaper.RefreshToolbar(integer command_id)
---
---
---See RefreshToolbar2
---.
function reaper.RefreshToolbar(command_id)
end


---Lua: reaper.RefreshToolbar2(integer section_id, integer command_id)
---
---
---Refresh the toolbar button states of a toggle action.
function reaper.RefreshToolbar2(section_id, command_id)
end


---Lua: string out = reaper.relative_fn(string in, string out)
---
---
---Makes a filename "in" relative to the current project, if any.
function reaper.relative_fn(In, out)
end


---Lua: boolean reaper.RemoveTrackSend(MediaTrack tr, integer category, integer sendidx)
---
---
---Remove a send/receive/hardware output, return true on success. category is <0 for receives, 0=sends, >0 for hardware outputs. See CreateTrackSend
---, GetSetTrackSendInfo
---, GetTrackSendInfo_Value
---, SetTrackSendInfo_Value
---, GetTrackNumSends
---.
function reaper.RemoveTrackSend(tr, category, sendidx)
end


---Lua: boolean reaper.RenderFileSection(string source_filename, string target_filename, number start_percent, number end_percent, number playrate)
---
---
---Not available while playing back.
function reaper.RenderFileSection(source_filename, target_filename, start_percent, end_percent, playrate)
end


---Lua: boolean reaper.ReorderSelectedTracks(integer beforeTrackIdx, integer makePrevFolder)
---
---
---Moves all selected tracks to immediately above track specified by index beforeTrackIdx, returns false if no tracks were selected. makePrevFolder=0 for normal, 1 = as child of track preceding track specified by beforeTrackIdx, 2 = if track preceding track specified by beforeTrackIdx is last track in folder, extend folder
function reaper.ReorderSelectedTracks(beforeTrackIdx, makePrevFolder)
end


---Lua: string reaper.Resample_EnumModes(integer mode)
function reaper.Resample_EnumModes(mode)
end


---Lua: string out = reaper.resolve_fn(string in, string out)
---
---
---See resolve_fn2
---.
function reaper.resolve_fn(In, out)
end


---Lua: string out = reaper.resolve_fn2(string in, string out, optional string checkSubDir)
---
---
---Resolves a filename "in" by using project settings etc. If no file found, out will be a copy of in.
function reaper.resolve_fn2(In, out, checkSubDir)
end


---Lua: string reaper.ReverseNamedCommandLookup(integer command_id)
---
---
---Get the named command for the given command ID. The returned string will not start with '_' (e.g. it will return "SWS_ABOUT"), it will be NULL if command_id is a native action.
function reaper.ReverseNamedCommandLookup(command_id)
end


---Lua: number reaper.ScaleFromEnvelopeMode(integer scaling_mode, number val)
---
---
---See GetEnvelopeScalingMode
---.
function reaper.ScaleFromEnvelopeMode(scaling_mode, val)
end


---Lua: number reaper.ScaleToEnvelopeMode(integer scaling_mode, number val)
---
---
---See GetEnvelopeScalingMode
---.
function reaper.ScaleToEnvelopeMode(scaling_mode, val)
end


---Lua: reaper.SelectAllMediaItems(ReaProject proj, boolean selected)
function reaper.SelectAllMediaItems(proj, selected)
end


---Lua: reaper.SelectProjectInstance(ReaProject proj)
function reaper.SelectProjectInstance(proj)
end


---Lua: reaper.SetActiveTake(MediaItem_Take take)
---
---
---set this take active in this media item
function reaper.SetActiveTake(take)
end


---Lua: reaper.SetAutomationMode(integer mode, boolean onlySel)
---
---
---sets all or selected tracks to mode.
function reaper.SetAutomationMode(mode, onlySel)
end


---Lua: reaper.SetCurrentBPM(ReaProject __proj, number bpm, boolean wantUndo)
---
---
---set current BPM in project, set wantUndo=true to add undo point
function reaper.SetCurrentBPM(__proj, bpm, wantUndo)
end


---Lua: reaper.SetCursorContext(integer mode, TrackEnvelope envIn)
---
---
---You must use this to change the focus programmatically. mode=0 to focus track panels, 1 to focus the arrange window, 2 to focus the arrange window and select env (or env==NULL to clear the current track/take envelope selection)
function reaper.SetCursorContext(mode, envIn)
end


---Lua: reaper.SetEditCurPos(number time, boolean moveview, boolean seekplay)
function reaper.SetEditCurPos(time, moveview, seekplay)
end


---Lua: reaper.SetEditCurPos2(ReaProject proj, number time, boolean moveview, boolean seekplay)
function reaper.SetEditCurPos2(proj, time, moveview, seekplay)
end


---Lua: boolean reaper.SetEnvelopePoint(TrackEnvelope envelope, integer ptidx, optional number timeIn, optional number valueIn, optional number shapeIn, optional number tensionIn, optional boolean selectedIn, optional boolean noSortIn)
---
---
---Set attributes of an envelope point. Values that are not supplied will be ignored. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done. See GetEnvelopePoint
---, InsertEnvelopePoint
---, GetEnvelopeScalingMode
---.
function reaper.SetEnvelopePoint(envelope, ptidx, timeIn, valueIn, shapeIn, tensionIn, selectedIn, noSortIn)
end


---Lua: boolean reaper.SetEnvelopePointEx(TrackEnvelope envelope, integer autoitem_idx, integer ptidx, optional number timeIn, optional number valueIn, optional number shapeIn, optional number tensionIn, optional boolean selectedIn, optional boolean noSortIn)
---
---
---Set attributes of an envelope point. Values that are not supplied will be ignored. If setting multiple points at once, set noSort=true, and call Envelope_SortPoints when done. Tautoitem_idx==-1 for the underlying envelope, 0 for the first automation item on the envelope, etc. See GetEnvelopePoint
---, InsertEnvelopePoint
---, GetEnvelopeScalingMode
---.
function reaper.SetEnvelopePointEx(envelope, autoitem_idx, ptidx, timeIn, valueIn, shapeIn, tensionIn, selectedIn, noSortIn)
end


---Lua: boolean reaper.SetEnvelopeStateChunk(TrackEnvelope env, string str, boolean isundo)
---
---
---Sets the RPPXML state of an envelope, returns true if successful. Undo flag is a performance/caching hint.
function reaper.SetEnvelopeStateChunk(env, str, isundo)
end


---Lua: reaper.SetExtState(string section, string key, string value, boolean persist)
---
---
---Set the extended state value for a specific section and key. persist=true means the value should be stored and reloaded the next time REAPER is opened. See GetExtState
---, DeleteExtState
---, HasExtState
---.
function reaper.SetExtState(section, key, value, persist)
end


---Lua: reaper.SetGlobalAutomationOverride(integer mode)
---
---
---mode: see GetGlobalAutomationOverride
function reaper.SetGlobalAutomationOverride(mode)
end


---Lua: boolean reaper.SetItemStateChunk(MediaItem item, string str, boolean isundo)
---
---
---Sets the RPPXML state of an item, returns true if successful. Undo flag is a performance/caching hint.
function reaper.SetItemStateChunk(item, str, isundo)
end


---Lua: integer reaper.SetMasterTrackVisibility(integer flag)
---
---
---set &1 to show the master track in the TCP, &2 to show in the mixer. Returns the previous visibility state. See GetMasterTrackVisibility
---.
function reaper.SetMasterTrackVisibility(flag)
end


---Lua: boolean reaper.SetMediaItemInfo_Value(MediaItem item, string parmname, number newvalue)
---
---
---Set media item numerical-value attributes.
---
---B_MUTE : bool * to muted state
---
---B_LOOPSRC : bool * to loop source
---
---B_ALLTAKESPLAY : bool * to all takes play
---
---B_UISEL : bool * to ui selected
---
---C_BEATATTACHMODE : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsosonly
---
---C_LOCK : char * to one char of lock flags (&1 is locked, currently)
---
---D_VOL : double * of item volume (volume bar)
---
---D_POSITION : double * of item position (seconds)
---
---D_LENGTH : double * of item length (seconds)
---
---D_SNAPOFFSET : double * of item snap offset (seconds)
---
---D_FADEINLEN : double * of item fade in length (manual, seconds)
---
---D_FADEOUTLEN : double * of item fade out length (manual, seconds)
---
---D_FADEINDIR : double * of item fade in curve [-1; 1]
---
---D_FADEOUTDIR : double * of item fade out curve [-1; 1]
---
---D_FADEINLEN_AUTO : double * of item autofade in length (seconds, -1 for no autofade set)
---
---D_FADEOUTLEN_AUTO : double * of item autofade out length (seconds, -1 for no autofade set)
---
---C_FADEINSHAPE : int * to fadein shape, 0=linear, ...
---
---C_FADEOUTSHAPE : int * to fadeout shape
---
---I_GROUPID : int * to group ID (0 = no group)
---
---I_LASTY : int * to last y position in track (readonly)
---
---I_LASTH : int * to last height in track (readonly)
---
---I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
---
---I_CURTAKE : int * to active take
---
---IP_ITEMNUMBER : int, item number within the track (read-only, returns the item number directly)
---
---F_FREEMODE_Y : float * to free mode y position (0..1)
---
---F_FREEMODE_H : float * to free mode height (0..1)
function reaper.SetMediaItemInfo_Value(item, parmname, newvalue)
end


---Lua: boolean reaper.SetMediaItemLength(MediaItem item, number length, boolean refreshUI)
---
---
---Redraws the screen only if refreshUI == true.
---
---See UpdateArrange
---().
function reaper.SetMediaItemLength(item, length, refreshUI)
end


---Lua: boolean reaper.SetMediaItemPosition(MediaItem item, number position, boolean refreshUI)
---
---
---Redraws the screen only if refreshUI == true.
---
---See UpdateArrange
---().
function reaper.SetMediaItemPosition(item, position, refreshUI)
end


---Lua: reaper.SetMediaItemSelected(MediaItem item, boolean selected)
function reaper.SetMediaItemSelected(item, selected)
end


---Lua: boolean reaper.SetMediaItemTake_Source(MediaItem_Take take, PCM_source source)
---
---
---Set media source of media item take
function reaper.SetMediaItemTake_Source(take, source)
end


---Lua: boolean reaper.SetMediaItemTakeInfo_Value(MediaItem_Take take, string parmname, number newvalue)
---
---
---Set media item take numerical-value attributes.
---
---D_STARTOFFS : double *, start offset in take of item
---
---D_VOL : double *, take volume
---
---D_PAN : double *, take pan
---
---D_PANLAW : double *, take pan law (-1.0=default, 0.5=-6dB, 1.0=+0dB, etc)
---
---D_PLAYRATE : double *, take playrate (1.0=normal, 2.0=doublespeed, etc)
---
---D_PITCH : double *, take pitch adjust (in semitones, 0.0=normal, +12 = one octave up, etc)
---
---B_PPITCH, bool *, preserve pitch when changing rate
---
---I_CHANMODE, int *, channel mode (0=normal, 1=revstereo, 2=downmix, 3=l, 4=r)
---
---I_PITCHMODE, int *, pitch shifter mode, -1=proj default, otherwise high word=shifter low word = parameter
---
---I_CUSTOMCOLOR : int *, custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
---
---IP_TAKENUMBER : int, take number within the item (read-only, returns the take number directly)
function reaper.SetMediaItemTakeInfo_Value(take, parmname, newvalue)
end


---Lua: boolean reaper.SetMediaTrackInfo_Value(MediaTrack tr, string parmname, number newvalue)
---
---
---Set track numerical-value attributes.
---
---B_MUTE : bool * : mute flag
---
---B_PHASE : bool * : invert track phase
---
---IP_TRACKNUMBER : int : track number (returns zero if not found, -1 for master track) (read-only, returns the int directly)
---
---I_SOLO : int * : 0=not soloed, 1=solo, 2=soloed in place. also: 5=solo-safe solo, 6=solo-safe soloed in place
---
---I_FXEN : int * : 0=fx bypassed, nonzero = fx active
---
---I_RECARM : int * : 0=not record armed, 1=record armed
---
---I_RECINPUT : int * : record input. <0 = no input, 0..n = mono hardware input, 512+n = rearoute input, 1024 set for stereo input pair. 4096 set for MIDI input, if set, then low 5 bits represent channel (0=all, 1-16=only chan), then next 6 bits represent physical input (63=all, 62=VKB)
---
---I_RECMODE : int * : record mode (0=input, 1=stereo out, 2=none, 3=stereo out w/latcomp, 4=midi output, 5=mono out, 6=mono out w/ lat comp, 7=midi overdub, 8=midi replace
---
---I_RECMON : int * : record monitor (0=off, 1=normal, 2=not when playing (tapestyle))
---
---I_RECMONITEMS : int * : monitor items while recording (0=off, 1=on)
---
---I_AUTOMODE : int * : track automation mode (0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
---
---I_NCHAN : int * : number of track channels, must be 2-64, even
---
---I_SELECTED : int * : track selected? 0 or 1
---
---I_WNDH : int * : current TCP window height (Read-only)
---
---I_FOLDERDEPTH : int * : folder depth change (0=normal, 1=track is a folder parent, -1=track is the last in the innermost folder, -2=track is the last in the innermost and next-innermost folders, etc
---
---I_FOLDERCOMPACT : int * : folder compacting (only valid on folders), 0=normal, 1=small, 2=tiny children
---
---I_MIDIHWOUT : int * : track midi hardware output index (<0 for disabled, low 5 bits are which channels (0=all, 1-16), next 5 bits are output device index (0-31))
---
---I_PERFFLAGS : int * : track perf flags (&1=no media buffering, &2=no anticipative FX)
---
---I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
---
---I_HEIGHTOVERRIDE : int * : custom height override for TCP window. 0 for none, otherwise size in pixels
---
---B_HEIGHTLOCK : bool * : track height lock (must set I_HEIGHTOVERRIDE before locking)
---
---D_VOL : double * : trim volume of track (0 (-inf)..1 (+0dB) .. 2 (+6dB) etc ..)
---
---D_PAN : double * : trim pan of track (-1..1)
---
---D_WIDTH : double * : width of track (-1..1)
---
---D_DUALPANL : double * : dualpan position 1 (-1..1), only if I_PANMODE==6
---
---D_DUALPANR : double * : dualpan position 2 (-1..1), only if I_PANMODE==6
---
---I_PANMODE : int * : pan mode (0 = classic 3.x, 3=new balance, 5=stereo pan, 6 = dual pan)
---
---D_PANLAW : double * : pan law of track. <0 for project default, 1.0 for +0dB, etc
---
---P_ENV : read only, returns TrackEnvelope *, setNewValue=<VOLENV, <PANENV, etc
---
---B_SHOWINMIXER : bool * : show track panel in mixer -- do not use on master
---
---B_SHOWINTCP : bool * : show track panel in tcp -- do not use on master
---
---B_MAINSEND : bool * : track sends audio to parent
---
---C_MAINSEND_OFFS : char * : track send to parent channel offset
---
---B_FREEMODE : bool * : track free-mode enabled (requires UpdateTimeline() after changing etc)
---
---C_BEATATTACHMODE : char * : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsposonly
---
---F_MCP_FXSEND_SCALE : float * : scale of fx+send area in MCP (0.0=smallest allowed, 1=max allowed)
---
---F_MCP_SENDRGN_SCALE : float * : scale of send area as proportion of the fx+send total area (0=min allow, 1=max)
function reaper.SetMediaTrackInfo_Value(tr, parmname, newvalue)
end


---Lua: reaper.SetMIDIEditorGrid(ReaProject project, number division)
---
---
---Set the MIDI editor grid division. 0.25=quarter note, 1.0/3.0=half note tripet, etc.
function reaper.SetMIDIEditorGrid(project, division)
end


---Lua: MediaTrack reaper.SetMixerScroll(MediaTrack leftmosttrack)
---
---
---Scroll the mixer so that leftmosttrack is the leftmost visible track. Returns the leftmost track after scrolling, which may be different from the passed-in track if there are not enough tracks to its right.
function reaper.SetMixerScroll(leftmosttrack)
end


---Lua: reaper.SetMouseModifier(string context, integer modifier_flag, string action)
---
---
---Set the mouse modifier assignment for a specific modifier key assignment, in a specific context.
---
---Context is a string like "MM_CTX_ITEM". Find these strings by modifying an assignment in
---
---Preferences/Editing/Mouse Modifiers, then looking in reaper-mouse.ini.
---
---Modifier flag is a number from 0 to 15: add 1 for shift, 2 for control, 4 for alt, 8 for win.
---
---(macOS: add 1 for shift, 2 for command, 4 for opt, 8 for control.)
---
---For left-click and double-click contexts, the action can be any built-in command ID number
---
---or any custom action ID string. Find built-in command IDs in the REAPER actions window
---
---(enable "show action IDs" in the context menu), and find custom action ID strings in reaper-kb.ini.
---
---For built-in mouse modifier behaviors, find action IDs (which will be low numbers)
---
---by modifying an assignment in Preferences/Editing/Mouse Modifiers, then looking in reaper-mouse.ini.
---
---Assigning an action of -1 will reset that mouse modifier behavior to factory default.
---
---See GetMouseModifier
---.
function reaper.SetMouseModifier(context, modifier_flag, action)
end


---Lua: reaper.SetOnlyTrackSelected(MediaTrack track)
---
---
---Set exactly one track selected, deselect all others
function reaper.SetOnlyTrackSelected(track)
end


---Lua: reaper.SetProjectGrid(ReaProject project, number division)
---
---
---Set the arrange view grid division. 0.25=quarter note, 1.0/3.0=half note triplet, etc.
function reaper.SetProjectGrid(project, division)
end


---Lua: boolean reaper.SetProjectMarker(integer markrgnindexnumber, boolean isrgn, number pos, number rgnend, string name)
function reaper.SetProjectMarker(markrgnindexnumber, isrgn, pos, rgnend, name)
end


---Lua: boolean reaper.SetProjectMarker2(ReaProject proj, integer markrgnindexnumber, boolean isrgn, number pos, number rgnend, string name)
function reaper.SetProjectMarker2(proj, markrgnindexnumber, isrgn, pos, rgnend, name)
end


---Lua: boolean reaper.SetProjectMarker3(ReaProject proj, integer markrgnindexnumber, boolean isrgn, number pos, number rgnend, string name, integer color)
function reaper.SetProjectMarker3(proj, markrgnindexnumber, isrgn, pos, rgnend, name, color)
end


---Lua: boolean reaper.SetProjectMarker4(ReaProject proj, integer markrgnindexnumber, boolean isrgn, number pos, number rgnend, string name, integer color, integer flags)
---
---
---color should be 0 to not change, or ColorToNative(r,g,b)|0x1000000, flags&1 to clear name
function reaper.SetProjectMarker4(proj, markrgnindexnumber, isrgn, pos, rgnend, name, color, flags)
end


---Lua: boolean reaper.SetProjectMarkerByIndex(ReaProject proj, integer markrgnidx, boolean isrgn, number pos, number rgnend, integer IDnumber, string name, integer color)
---
---
---See SetProjectMarkerByIndex2
---.
function reaper.SetProjectMarkerByIndex(proj, markrgnidx, isrgn, pos, rgnend, IDnumber, name, color)
end


---Lua: boolean reaper.SetProjectMarkerByIndex2(ReaProject proj, integer markrgnidx, boolean isrgn, number pos, number rgnend, integer IDnumber, string name, integer color, integer flags)
---
---
---Differs from SetProjectMarker4 in that markrgnidx is 0 for the first marker/region, 1 for the next, etc (see EnumProjectMarkers3
---), rather than representing the displayed marker/region ID number (see SetProjectMarker3
---). Function will fail if attempting to set a duplicate ID number for a region (duplicate ID numbers for markers are OK). , flags&1 to clear name.
function reaper.SetProjectMarkerByIndex2(proj, markrgnidx, isrgn, pos, rgnend, IDnumber, name, color, flags)
end


---Lua: integer reaper.SetProjExtState(ReaProject proj, string extname, string key, string value)
---
---
---Save a key/value pair for a specific extension, to be restored the next time this specific project is loaded. Typically extname will be the name of a reascript or extension section. If key is NULL or "", all extended data for that extname will be deleted.  If val is NULL or "", the data previously associated with that key will be deleted. Returns the size of the state for this extname. See GetProjExtState
---, EnumProjExtState
---.
function reaper.SetProjExtState(proj, extname, key, value)
end


---Lua: reaper.SetRegionRenderMatrix(ReaProject proj, integer regionindex, MediaTrack track, integer addorremove)
---
---
---Add (addorremove > 0) or remove (addorremove < 0) a track from this region when using the region render matrix.
function reaper.SetRegionRenderMatrix(proj, regionindex, track, addorremove)
end


---Lua: integer reaper.SetTakeStretchMarker(MediaItem_Take take, integer idx, number pos, optional number srcposIn)
---
---
---Adds or updates a stretch marker. If idx<0, stretch marker will be added. If idx>=0, stretch marker will be updated. When adding, if srcposInOptional is omitted, source position will be auto-calculated. When updating a stretch marker, if srcposInOptional is omitted, srcpos will not be modified. Position/srcposition values will be constrained to nearby stretch markers. Returns index of stretch marker, or -1 if did not insert (or marker already existed at time).
function reaper.SetTakeStretchMarker(take, idx, pos, srcposIn)
end


---Lua: boolean reaper.SetTakeStretchMarkerSlope(MediaItem_Take take, integer idx, number slope)
---
---
---See GetTakeStretchMarkerSlope
function reaper.SetTakeStretchMarkerSlope(take, idx, slope)
end


---Lua: boolean reaper.SetTempoTimeSigMarker(ReaProject proj, integer ptidx, number timepos, integer measurepos, number beatpos, number bpm, integer timesig_num, integer timesig_denom, boolean lineartempo)
---
---
---Set parameters of a tempo/time signature marker. Provide either timepos (with measurepos=-1, beatpos=-1), or measurepos and beatpos (with timepos=-1). If timesig_num and timesig_denom are zero, the previous time signature will be used. ptidx=-1 will insert a new tempo/time signature marker. See CountTempoTimeSigMarkers
---, GetTempoTimeSigMarker
---, AddTempoTimeSigMarker
---.
function reaper.SetTempoTimeSigMarker(proj, ptidx, timepos, measurepos, beatpos, bpm, timesig_num, timesig_denom, lineartempo)
end


---Lua: boolean reaper.SetToggleCommandState(integer section_id, integer command_id, integer state)
---
---
---Updates the toggle state of an action, returns true if succeeded. Only ReaScripts can have their toggle states changed programmatically. See RefreshToolbar2
---.
function reaper.SetToggleCommandState(section_id, command_id, state)
end


---Lua: reaper.SetTrackAutomationMode(MediaTrack tr, integer mode)
function reaper.SetTrackAutomationMode(tr, mode)
end


---Lua: reaper.SetTrackColor(MediaTrack track, integer color)
---
---
---Set the custom track color, color is OS dependent (i.e. ColorToNative(r,g,b).
function reaper.SetTrackColor(track, color)
end


---Lua: boolean reaper.SetTrackMIDILyrics(MediaTrack track, integer flag, string str)
---
---
---Set all MIDI lyrics on the track. Lyrics will be stuffed into any MIDI items found in range. Flag is unused at present. str is passed in as beat position, tab, text, tab (example with flag=2: "1.1.2\tLyric for measure 1 beat 2\t.1.1\tLyric for measure 2 beat 1	"). See GetTrackMIDILyrics
function reaper.SetTrackMIDILyrics(track, flag, str)
end


---Lua: boolean reaper.SetTrackMIDINoteName(integer track, integer pitch, integer chan, string name)
---
---
---channel < 0 assigns these note names to all channels.
function reaper.SetTrackMIDINoteName(track, pitch, chan, name)
end


---Lua: boolean reaper.SetTrackMIDINoteNameEx(ReaProject proj, MediaTrack track, integer pitch, integer chan, string name)
---
---
---channel < 0 assigns note name to all channels. pitch 128 assigns name for CC0, pitch 129 for CC1, etc.
function reaper.SetTrackMIDINoteNameEx(proj, track, pitch, chan, name)
end


---Lua: reaper.SetTrackSelected(MediaTrack track, boolean selected)
function reaper.SetTrackSelected(track, selected)
end


---Lua: boolean reaper.SetTrackSendInfo_Value(MediaTrack tr, integer category, integer sendidx, string parmname, number newvalue)
---
---
---Set send/receive/hardware output numerical-value attributes, return true on success.
---
---category is <0 for receives, 0=sends, >0 for hardware outputs
---
---parameter names:
---
---B_MUTE : returns bool *
---
---B_PHASE : returns bool *, true to flip phase
---
---B_MONO : returns bool *
---
---D_VOL : returns double *, 1.0 = +0dB etc
---
---D_PAN : returns double *, -1..+1
---
---D_PANLAW : returns double *,1.0=+0.0db, 0.5=-6dB, -1.0 = projdef etc
---
---I_SENDMODE : returns int *, 0=post-fader, 1=pre-fx, 2=post-fx (deprecated), 3=post-fx
---
---I_AUTOMODE : returns int * : automation mode (-1=use track automode, 0=trim/off, 1=read, 2=touch, 3=write, 4=latch)
---
---I_SRCCHAN : returns int *, index,&1024=mono, -1 for none
---
---I_DSTCHAN : returns int *, index, &1024=mono, otherwise stereo pair, hwout:&512=rearoute
---
---I_MIDIFLAGS : returns int *, low 5 bits=source channel 0=all, 1-16, next 5 bits=dest channel, 0=orig, 1-16=chanSee CreateTrackSend
---, RemoveTrackSend
---, GetTrackNumSends
---.
function reaper.SetTrackSendInfo_Value(tr, category, sendidx, parmname, newvalue)
end


---Lua: boolean reaper.SetTrackSendUIPan(MediaTrack track, integer send_idx, number pan, integer isend)
---
---
---send_idx<0 for receives, >=0 for hw ouputs, >=nb_of_hw_ouputs for sends. isend=1 for end of edit, -1 for an instant edit (such as reset), 0 for normal tweak.
function reaper.SetTrackSendUIPan(track, send_idx, pan, isend)
end


---Lua: boolean reaper.SetTrackSendUIVol(MediaTrack track, integer send_idx, number vol, integer isend)
---
---
---send_idx<0 for receives, >=0 for hw ouputs, >=nb_of_hw_ouputs for sends. isend=1 for end of edit, -1 for an instant edit (such as reset), 0 for normal tweak.
function reaper.SetTrackSendUIVol(track, send_idx, vol, isend)
end


---Lua: boolean reaper.SetTrackStateChunk(MediaTrack track, string str, boolean isundo)
---
---
---Sets the RPPXML state of a track, returns true if successful. Undo flag is a performance/caching hint.
function reaper.SetTrackStateChunk(track, str, isundo)
end


---Lua: reaper.ShowActionList(KbdSectionInfo caller, HWND callerWnd)
function reaper.ShowActionList(caller, callerWnd)
end


---Lua: reaper.ShowConsoleMsg(string msg)
---
---
---Show a message to the user (also useful for debugging). Send "\n" for newline, "" to clear the console. See ClearConsole
function reaper.ShowConsoleMsg(msg)
end


---Lua: integer reaper.ShowMessageBox(string msg, string title, integer type)
---
---
---type 0=OK,1=OKCANCEL,2=ABORTRETRYIGNORE,3=YESNOCANCEL,4=YESNO,5=RETRYCANCEL : ret 1=OK,2=CANCEL,3=ABORT,4=RETRY,5=IGNORE,6=YES,7=NO
function reaper.ShowMessageBox(msg, title, type)
end


---Lua: reaper.ShowPopupMenu(string name, integer x, integer y, HWND hwndParent, identifier ctx, integer ctx2, integer ctx3)
---
---
---shows a context menu, valid names include: track_input, track_panel, track_area, track_routing, item, ruler, envelope, envelope_point, envelope_item. ctxOptional can be a track pointer for track_*, item pointer for item* (but is optional). for envelope_point, ctx2Optional has point index, ctx3Optional has item index (0=main envelope, 1=first AI). for envelope_item, ctx2Optional has AI index (1=first AI)
function reaper.ShowPopupMenu(name, x, y, hwndParent, ctx, ctx2, ctx3)
end


---Lua: number reaper.SLIDER2DB(number y)
function reaper.SLIDER2DB(y)
end


---Lua: number reaper.SnapToGrid(ReaProject project, number time_pos)
function reaper.SnapToGrid(project, time_pos)
end


---Lua: reaper.SoloAllTracks(integer solo)
---
---
---solo=2 for SIP
function reaper.SoloAllTracks(solo)
end


---Lua: HWND reaper.Splash_GetWnd()
---
---
---gets the splash window, in case you want to display a message over it. Returns NULL when the sphah window is not displayed.
function reaper.Splash_GetWnd()
end


---Lua: MediaItem reaper.SplitMediaItem(MediaItem item, number position)
---
---
---the original item becomes the left-hand split, the function returns the right-hand split (or NULL if the split failed)
function reaper.SplitMediaItem(item, position)
end


---Lua: string gGUID = reaper.stringToGuid(string str, string gGUID)
function reaper.stringToGuid(str, gGUID)
end


---Lua: reaper.StuffMIDIMessage(integer mode, integer msg1, integer msg2, integer msg3)
---
---
---Stuffs a 3 byte MIDI message into either the Virtual MIDI Keyboard queue, or the MIDI-as-control input queue, or sends to a MIDI hardware output. mode=0 for VKB, 1 for control (actions map etc), 2 for VKB-on-current-channel; 16 for external MIDI device 0, 17 for external MIDI device 1, etc; see GetNumMIDIOutputs
---, GetMIDIOutputName
---.
function reaper.StuffMIDIMessage(mode, msg1, msg2, msg3)
end


---Lua: integer reaper.TakeFX_AddByName(MediaItem_Take take, string fxname, integer instantiate)
---
---
---Adds or queries the position of a named FX in a take. Specify a negative value for instantiate to always create a new effect, 0 to only query the first instance of an effect, or a positive value to add an instance if one is not found.
function reaper.TakeFX_AddByName(take, fxname, instantiate)
end


---Lua: reaper.TakeFX_CopyToTake(MediaItem_Take src_take, integer src_fx, MediaItem_Take dest_take, integer dest_fx, boolean is_move)
---
---
---Copies (or moves) FX from src_take to dest_take. Can be used with src_track=dest_track to reorder.
function reaper.TakeFX_CopyToTake(src_take, src_fx, dest_take, dest_fx, is_move)
end


---Lua: reaper.TakeFX_CopyToTrack(MediaItem_Take src_take, integer src_fx, MediaTrack dest_track, integer dest_fx, boolean is_move)
---
---
---Copies (or moves) FX from src_take to dest_track. dest_fx can have 0x1000000 set to reference input FX.
function reaper.TakeFX_CopyToTrack(src_take, src_fx, dest_track, dest_fx, is_move)
end


---Lua: boolean reaper.TakeFX_Delete(MediaItem_Take take, integer fx)
---
---
---Remove a FX from take chain (returns true on success)
function reaper.TakeFX_Delete(take, fx)
end


---Lua: boolean reaper.TakeFX_EndParamEdit(MediaItem_Take take, integer fx, integer param)
function reaper.TakeFX_EndParamEdit(take, fx, param)
end


---Lua: boolean retval, string buf = reaper.TakeFX_FormatParamValue(MediaItem_Take take, integer fx, integer param, number val, string buf)
---
---
---Note: only works with FX that support Cockos VST extensions.
function reaper.TakeFX_FormatParamValue(take, fx, param, val, buf)
end


---Lua: boolean retval, string buf = reaper.TakeFX_FormatParamValueNormalized(MediaItem_Take take, integer fx, integer param, number value, string buf)
---
---
---Note: only works with FX that support Cockos VST extensions.
function reaper.TakeFX_FormatParamValueNormalized(take, fx, param, value, buf)
end


---Lua: integer reaper.TakeFX_GetChainVisible(MediaItem_Take take)
---
---
---returns index of effect visible in chain, or -1 for chain hidden, or -2 for chain visible but no effect selected
function reaper.TakeFX_GetChainVisible(take)
end


---Lua: integer reaper.TakeFX_GetCount(MediaItem_Take take)
function reaper.TakeFX_GetCount(take)
end


---Lua: boolean reaper.TakeFX_GetEnabled(MediaItem_Take take, integer fx)
---
---
---See TakeFX_SetEnabled
function reaper.TakeFX_GetEnabled(take, fx)
end


---Lua: TrackEnvelope reaper.TakeFX_GetEnvelope(MediaItem_Take take, integer fxindex, integer parameterindex, boolean create)
---
---
---Returns the FX parameter envelope. If the envelope does not exist and create=true, the envelope will be created.
function reaper.TakeFX_GetEnvelope(take, fxindex, parameterindex, create)
end


---Lua: HWND reaper.TakeFX_GetFloatingWindow(MediaItem_Take take, integer index)
---
---
---returns HWND of floating window for effect index, if any
function reaper.TakeFX_GetFloatingWindow(take, index)
end


---Lua: boolean retval, string buf = reaper.TakeFX_GetFormattedParamValue(MediaItem_Take take, integer fx, integer param, string buf)
function reaper.TakeFX_GetFormattedParamValue(take, fx, param, buf)
end


---Lua: string GUID = reaper.TakeFX_GetFXGUID(MediaItem_Take take, integer fx)
function reaper.TakeFX_GetFXGUID(take, fx)
end


---Lua: boolean retval, string buf = reaper.TakeFX_GetFXName(MediaItem_Take take, integer fx, string buf)
function reaper.TakeFX_GetFXName(take, fx, buf)
end


---Lua: integer retval, optional number inputPins, optional number outputPins = reaper.TakeFX_GetIOSize(MediaItem_Take take, integer fx)
---
---
---sets the number of input/output pins for FX if available, returns plug-in type or -1 on error
function reaper.TakeFX_GetIOSize(take, fx)
end


---Lua: boolean retval, string buf = reaper.TakeFX_GetNamedConfigParm(MediaItem_Take take, integer fx, string parmname)
---
---
---gets plug-in specific named configuration value (returns true on success). see TrackFX_GetNamedConfigParm
function reaper.TakeFX_GetNamedConfigParm(take, fx, parmname)
end


---Lua: integer reaper.TakeFX_GetNumParams(MediaItem_Take take, integer fx)
function reaper.TakeFX_GetNumParams(take, fx)
end


---Lua: boolean reaper.TakeFX_GetOffline(MediaItem_Take take, integer fx)
---
---
---See TakeFX_SetOffline
function reaper.TakeFX_GetOffline(take, fx)
end


---Lua: boolean reaper.TakeFX_GetOpen(MediaItem_Take take, integer fx)
---
---
---Returns true if this FX UI is open in the FX chain window or a floating window. See TakeFX_SetOpen
function reaper.TakeFX_GetOpen(take, fx)
end


---Lua: number retval, number minval, number maxval = reaper.TakeFX_GetParam(MediaItem_Take take, integer fx, integer param)
function reaper.TakeFX_GetParam(take, fx, param)
end


---Lua: boolean retval, number step, number smallstep, number largestep, boolean istoggle = reaper.TakeFX_GetParameterStepSizes(MediaItem_Take take, integer fx, integer param)
function reaper.TakeFX_GetParameterStepSizes(take, fx, param)
end


---Lua: number retval, number minval, number maxval, number midval = reaper.TakeFX_GetParamEx(MediaItem_Take take, integer fx, integer param)
function reaper.TakeFX_GetParamEx(take, fx, param)
end


---Lua: boolean retval, string buf = reaper.TakeFX_GetParamName(MediaItem_Take take, integer fx, integer param, string buf)
function reaper.TakeFX_GetParamName(take, fx, param, buf)
end


---Lua: number reaper.TakeFX_GetParamNormalized(MediaItem_Take take, integer fx, integer param)
function reaper.TakeFX_GetParamNormalized(take, fx, param)
end


---Lua: integer retval, optional number high32 = reaper.TakeFX_GetPinMappings(MediaItem_Take tr, integer fx, integer isoutput, integer pin)
---
---
---gets the effective channel mapping bitmask for a particular pin. high32OutOptional will be set to the high 32 bits
function reaper.TakeFX_GetPinMappings(tr, fx, isoutput, pin)
end


---Lua: boolean retval, string presetname = reaper.TakeFX_GetPreset(MediaItem_Take take, integer fx, string presetname)
---
---
---Get the name of the preset currently showing in the REAPER dropdown, or the full path to a factory preset file for VST3 plug-ins (.vstpreset). Returns false if the current FX parameters do not exactly match the preset (in other words, if the user loaded the preset but moved the knobs afterward). See TakeFX_SetPreset
---.
function reaper.TakeFX_GetPreset(take, fx, presetname)
end


---Lua: integer retval, number numberOfPresets = reaper.TakeFX_GetPresetIndex(MediaItem_Take take, integer fx)
---
---
---Returns current preset index, or -1 if error. numberOfPresetsOut will be set to total number of presets available. See TakeFX_SetPresetByIndex
function reaper.TakeFX_GetPresetIndex(take, fx)
end


---Lua: string fn = reaper.TakeFX_GetUserPresetFilename(MediaItem_Take take, integer fx, string fn)
function reaper.TakeFX_GetUserPresetFilename(take, fx, fn)
end


---Lua: boolean reaper.TakeFX_NavigatePresets(MediaItem_Take take, integer fx, integer presetmove)
---
---
---presetmove==1 activates the next preset, presetmove==-1 activates the previous preset, etc.
function reaper.TakeFX_NavigatePresets(take, fx, presetmove)
end


---Lua: reaper.TakeFX_SetEnabled(MediaItem_Take take, integer fx, boolean enabled)
---
---
---See TakeFX_GetEnabled
function reaper.TakeFX_SetEnabled(take, fx, enabled)
end


---Lua: boolean reaper.TakeFX_SetNamedConfigParm(MediaItem_Take take, integer fx, string parmname, string value)
---
---
---gets plug-in specific named configuration value (returns true on success)
function reaper.TakeFX_SetNamedConfigParm(take, fx, parmname, value)
end


---Lua: reaper.TakeFX_SetOffline(MediaItem_Take take, integer fx, boolean offline)
---
---
---See TakeFX_GetOffline
function reaper.TakeFX_SetOffline(take, fx, offline)
end


---Lua: reaper.TakeFX_SetOpen(MediaItem_Take take, integer fx, boolean open)
---
---
---Open this FX UI. See TakeFX_GetOpen
function reaper.TakeFX_SetOpen(take, fx, open)
end


---Lua: boolean reaper.TakeFX_SetParam(MediaItem_Take take, integer fx, integer param, number val)
function reaper.TakeFX_SetParam(take, fx, param, val)
end


---Lua: boolean reaper.TakeFX_SetParamNormalized(MediaItem_Take take, integer fx, integer param, number value)
function reaper.TakeFX_SetParamNormalized(take, fx, param, value)
end


---Lua: boolean reaper.TakeFX_SetPinMappings(MediaItem_Take tr, integer fx, integer isoutput, integer pin, integer low32bits, integer hi32bits)
---
---
---sets the channel mapping bitmask for a particular pin. returns false if unsupported (not all types of plug-ins support this capability)
function reaper.TakeFX_SetPinMappings(tr, fx, isoutput, pin, low32bits, hi32bits)
end


---Lua: boolean reaper.TakeFX_SetPreset(MediaItem_Take take, integer fx, string presetname)
---
---
---Activate a preset with the name shown in the REAPER dropdown. Full paths to .vstpreset files are also supported for VST3 plug-ins. See TakeFX_GetPreset
---.
function reaper.TakeFX_SetPreset(take, fx, presetname)
end


---Lua: boolean reaper.TakeFX_SetPresetByIndex(MediaItem_Take take, integer fx, integer idx)
---
---
---Sets the preset idx, or the factory preset (idx==-2), or the default user preset (idx==-1). Returns true on success. See TakeFX_GetPresetIndex
---.
function reaper.TakeFX_SetPresetByIndex(take, fx, idx)
end


---Lua: reaper.TakeFX_Show(MediaItem_Take take, integer index, integer showFlag)
---
---
---showflag=0 for hidechain, =1 for show chain(index valid), =2 for hide floating window(index valid), =3 for show floating window (index valid)
function reaper.TakeFX_Show(take, index, showFlag)
end


---Lua: boolean reaper.TakeIsMIDI(MediaItem_Take take)
---
---
---Returns true if the active take contains MIDI.
function reaper.TakeIsMIDI(take)
end


---Lua: number reaper.time_precise()
---
---
---Gets a precise system timestamp in seconds
function reaper.time_precise()
end


---Lua: number reaper.TimeMap2_beatsToTime(ReaProject proj, number tpos, optional number measuresIn)
---
---
---convert a beat position (or optionally a beats+measures if measures is non-NULL) to time.
function reaper.TimeMap2_beatsToTime(proj, tpos, measuresIn)
end


---Lua: number reaper.TimeMap2_GetDividedBpmAtTime(ReaProject proj, number time)
---
---
---get the effective BPM at the time (seconds) position (i.e. 2x in /8 signatures)
function reaper.TimeMap2_GetDividedBpmAtTime(proj, time)
end


---Lua: number reaper.TimeMap2_GetNextChangeTime(ReaProject proj, number time)
---
---
---when does the next time map (tempo or time sig) change occur
function reaper.TimeMap2_GetNextChangeTime(proj, time)
end


---Lua: number reaper.TimeMap2_QNToTime(ReaProject proj, number qn)
---
---
---converts project QN position to time.
function reaper.TimeMap2_QNToTime(proj, qn)
end


---Lua: number retval, optional number measures, optional number cml, optional number fullbeats, optional number cdenom = reaper.TimeMap2_timeToBeats(ReaProject proj, number tpos)
---
---
---convert a time into beats.
---
---if measures is non-NULL, measures will be set to the measure count, return value will be beats since measure.
---
---if cml is non-NULL, will be set to current measure length in beats (i.e. time signature numerator)
---
---if fullbeats is non-NULL, and measures is non-NULL, fullbeats will get the full beat count (same value returned if measures is NULL).
---
---if cdenom is non-NULL, will be set to the current time signature denominator.
function reaper.TimeMap2_timeToBeats(proj, tpos)
end


---Lua: number reaper.TimeMap2_timeToQN(ReaProject proj, number tpos)
---
---
---converts project time position to QN position.
function reaper.TimeMap2_timeToQN(proj, tpos)
end


---Lua: number retval, optional boolean dropFrame = reaper.TimeMap_curFrameRate(ReaProject proj)
---
---
---Gets project framerate, and optionally whether it is drop-frame timecode
function reaper.TimeMap_curFrameRate(proj)
end


---Lua: number reaper.TimeMap_GetDividedBpmAtTime(number time)
---
---
---get the effective BPM at the time (seconds) position (i.e. 2x in /8 signatures)
function reaper.TimeMap_GetDividedBpmAtTime(time)
end


---Lua: number retval, number qn_start, number qn_end, number timesig_num, number timesig_denom, number tempo = reaper.TimeMap_GetMeasureInfo(ReaProject proj, integer measure)
---
---
---Get the QN position and time signature information for the start of a measure. Return the time in seconds of the measure start.
function reaper.TimeMap_GetMeasureInfo(proj, measure)
end


---Lua: integer retval, string pattern = reaper.TimeMap_GetMetronomePattern(ReaProject proj, number time, string pattern)
---
---
---Fills in a string representing the active metronome pattern. For example, in a 7/8 measure divided 3+4, the pattern might be "1221222". The length of the string is the time signature numerator, and the function returns the time signature denominator.
function reaper.TimeMap_GetMetronomePattern(proj, time, pattern)
end


---Lua: number timesig_num, number timesig_denom, number tempo = reaper.TimeMap_GetTimeSigAtTime(ReaProject proj, number time)
---
---
---get the effective time signature and tempo
function reaper.TimeMap_GetTimeSigAtTime(proj, time)
end


---Lua: integer retval, optional number qnMeasureStart, optional number qnMeasureEnd = reaper.TimeMap_QNToMeasures(ReaProject proj, number qn)
---
---
---Find which measure the given QN position falls in.
function reaper.TimeMap_QNToMeasures(proj, qn)
end


---Lua: number reaper.TimeMap_QNToTime(number qn)
---
---
---converts project QN position to time.
function reaper.TimeMap_QNToTime(qn)
end


---Lua: number reaper.TimeMap_QNToTime_abs(ReaProject proj, number qn)
---
---
---Converts project quarter note count (QN) to time. QN is counted from the start of the project, regardless of any partial measures. See TimeMap2_QNToTime
function reaper.TimeMap_QNToTime_abs(proj, qn)
end


---Lua: number reaper.TimeMap_timeToQN(number tpos)
---
---
---converts project QN position to time.
function reaper.TimeMap_timeToQN(tpos)
end


---Lua: number reaper.TimeMap_timeToQN_abs(ReaProject proj, number tpos)
---
---
---Converts project time position to quarter note count (QN). QN is counted from the start of the project, regardless of any partial measures. See TimeMap2_timeToQN
function reaper.TimeMap_timeToQN_abs(proj, tpos)
end


---Lua: boolean reaper.ToggleTrackSendUIMute(MediaTrack track, integer send_idx)
---
---
---send_idx<0 for receives, >=0 for hw ouputs, >=nb_of_hw_ouputs for sends.
function reaper.ToggleTrackSendUIMute(track, send_idx)
end


---Lua: number reaper.Track_GetPeakHoldDB(MediaTrack track, integer channel, boolean clear)
function reaper.Track_GetPeakHoldDB(track, channel, clear)
end


---Lua: number reaper.Track_GetPeakInfo(MediaTrack track, integer channel)
function reaper.Track_GetPeakInfo(track, channel)
end


---Lua: reaper.TrackCtl_SetToolTip(string fmt, integer xpos, integer ypos, boolean topmost)
---
---
---displays tooltip at location, or removes if empty string
function reaper.TrackCtl_SetToolTip(fmt, xpos, ypos, topmost)
end


---Lua: integer reaper.TrackFX_AddByName(MediaTrack track, string fxname, boolean recFX, integer instantiate)
---
---
---Adds or queries the position of a named FX from the track FX chain (recFX=false) or record input FX/monitoring FX (recFX=true, monitoring FX are on master track). Specify a negative value for instantiate to always create a new effect, 0 to only query the first instance of an effect, or a positive value to add an instance if one is not found. fxname can have prefix to specify type: VST3:,VST2:,VST:,AU:,JS:, or DX:.
function reaper.TrackFX_AddByName(track, fxname, recFX, instantiate)
end


---Lua: reaper.TrackFX_CopyToTake(MediaTrack src_track, integer src_fx, MediaItem_Take dest_take, integer dest_fx, boolean is_move)
---
---
---Copies (or moves) FX from src_track to dest_take. src_fx can have 0x1000000 set to reference input FX.
function reaper.TrackFX_CopyToTake(src_track, src_fx, dest_take, dest_fx, is_move)
end


---Lua: reaper.TrackFX_CopyToTrack(MediaTrack src_track, integer src_fx, MediaTrack dest_track, integer dest_fx, boolean is_move)
---
---
---Copies (or moves) FX from src_track to dest_track. Can be used with src_track=dest_track to reorder, FX indices have 0x1000000 set to reference input FX.
function reaper.TrackFX_CopyToTrack(src_track, src_fx, dest_track, dest_fx, is_move)
end


---Lua: boolean reaper.TrackFX_Delete(MediaTrack track, integer fx)
---
---
---Remove a FX from track chain (returns true on success)
function reaper.TrackFX_Delete(track, fx)
end


---Lua: boolean reaper.TrackFX_EndParamEdit(MediaTrack track, integer fx, integer param)
function reaper.TrackFX_EndParamEdit(track, fx, param)
end


---Lua: boolean retval, string buf = reaper.TrackFX_FormatParamValue(MediaTrack track, integer fx, integer param, number val, string buf)
---
---
---Note: only works with FX that support Cockos VST extensions.
function reaper.TrackFX_FormatParamValue(track, fx, param, val, buf)
end


---Lua: boolean retval, string buf = reaper.TrackFX_FormatParamValueNormalized(MediaTrack track, integer fx, integer param, number value, string buf)
---
---
---Note: only works with FX that support Cockos VST extensions.
function reaper.TrackFX_FormatParamValueNormalized(track, fx, param, value, buf)
end


---Lua: integer reaper.TrackFX_GetByName(MediaTrack track, string fxname, boolean instantiate)
---
---
---Get the index of the first track FX insert that matches fxname. If the FX is not in the chain and instantiate is true, it will be inserted. See TrackFX_GetInstrument
---, TrackFX_GetEQ
---. Deprecated in favor of TrackFX_AddByName.
function reaper.TrackFX_GetByName(track, fxname, instantiate)
end


---Lua: integer reaper.TrackFX_GetChainVisible(MediaTrack track)
---
---
---returns index of effect visible in chain, or -1 for chain hidden, or -2 for chain visible but no effect selected
function reaper.TrackFX_GetChainVisible(track)
end


---Lua: integer reaper.TrackFX_GetCount(MediaTrack track)
function reaper.TrackFX_GetCount(track)
end


---Lua: boolean reaper.TrackFX_GetEnabled(MediaTrack track, integer fx)
---
---
---See TrackFX_SetEnabled
function reaper.TrackFX_GetEnabled(track, fx)
end


---Lua: integer reaper.TrackFX_GetEQ(MediaTrack track, boolean instantiate)
---
---
---Get the index of ReaEQ in the track FX chain. If ReaEQ is not in the chain and instantiate is true, it will be inserted. See TrackFX_GetInstrument
---, TrackFX_GetByName
---.
function reaper.TrackFX_GetEQ(track, instantiate)
end


---Lua: boolean reaper.TrackFX_GetEQBandEnabled(MediaTrack track, integer fxidx, integer bandtype, integer bandidx)
---
---
---Returns true if the EQ band is enabled.
---
---Returns false if the band is disabled, or if track/fxidx is not ReaEQ.
---
---Bandtype: 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
---
---Bandidx: 0=first band matching bandtype, 1=2nd band matching bandtype, etc.
---
---See TrackFX_GetEQ
---, TrackFX_GetEQParam
---, TrackFX_SetEQParam
---, TrackFX_SetEQBandEnabled
---.
function reaper.TrackFX_GetEQBandEnabled(track, fxidx, bandtype, bandidx)
end


---Lua: boolean retval, number bandtype, number bandidx, number paramtype, number normval = reaper.TrackFX_GetEQParam(MediaTrack track, integer fxidx, integer paramidx)
---
---
---Returns false if track/fxidx is not ReaEQ.
---
---Bandtype: -1=master gain, 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
---
---Bandidx (ignored for master gain): 0=first band matching bandtype, 1=2nd band matching bandtype, etc.
---
---Paramtype (ignored for master gain): 0=freq, 1=gain, 2=Q.
---
---See TrackFX_GetEQ
---, TrackFX_SetEQParam
---, TrackFX_GetEQBandEnabled
---, TrackFX_SetEQBandEnabled
---.
function reaper.TrackFX_GetEQParam(track, fxidx, paramidx)
end


---Lua: HWND reaper.TrackFX_GetFloatingWindow(MediaTrack track, integer index)
---
---
---returns HWND of floating window for effect index, if any
function reaper.TrackFX_GetFloatingWindow(track, index)
end


---Lua: boolean retval, string buf = reaper.TrackFX_GetFormattedParamValue(MediaTrack track, integer fx, integer param, string buf)
function reaper.TrackFX_GetFormattedParamValue(track, fx, param, buf)
end


---Lua: string GUID = reaper.TrackFX_GetFXGUID(MediaTrack track, integer fx)
function reaper.TrackFX_GetFXGUID(track, fx)
end


---Lua: boolean retval, string buf = reaper.TrackFX_GetFXName(MediaTrack track, integer fx, string buf)
function reaper.TrackFX_GetFXName(track, fx, buf)
end


---Lua: integer reaper.TrackFX_GetInstrument(MediaTrack track)
---
---
---Get the index of the first track FX insert that is a virtual instrument, or -1 if none. See TrackFX_GetEQ
---, TrackFX_GetByName
---.
function reaper.TrackFX_GetInstrument(track)
end


---Lua: integer retval, optional number inputPins, optional number outputPins = reaper.TrackFX_GetIOSize(MediaTrack track, integer fx)
---
---
---sets the number of input/output pins for FX if available, returns plug-in type or -1 on error
function reaper.TrackFX_GetIOSize(track, fx)
end


---Lua: boolean retval, string buf = reaper.TrackFX_GetNamedConfigParm(MediaTrack track, integer fx, string parmname)
---
---
---gets plug-in specific named configuration value (returns true on success). Special values: 'pdc' returns PDC latency. 'in_pin_0' returns name of first input pin (if available), 'out_pin_0' returns name of first output pin (if available), etc.
function reaper.TrackFX_GetNamedConfigParm(track, fx, parmname)
end


---Lua: integer reaper.TrackFX_GetNumParams(MediaTrack track, integer fx)
function reaper.TrackFX_GetNumParams(track, fx)
end


---Lua: boolean reaper.TrackFX_GetOffline(MediaTrack track, integer fx)
---
---
---See TrackFX_SetOffline
function reaper.TrackFX_GetOffline(track, fx)
end


---Lua: boolean reaper.TrackFX_GetOpen(MediaTrack track, integer fx)
---
---
---Returns true if this FX UI is open in the FX chain window or a floating window. See TrackFX_SetOpen
function reaper.TrackFX_GetOpen(track, fx)
end


---Lua: number retval, number minval, number maxval = reaper.TrackFX_GetParam(MediaTrack track, integer fx, integer param)
function reaper.TrackFX_GetParam(track, fx, param)
end


---Lua: boolean retval, number step, number smallstep, number largestep, boolean istoggle = reaper.TrackFX_GetParameterStepSizes(MediaTrack track, integer fx, integer param)
function reaper.TrackFX_GetParameterStepSizes(track, fx, param)
end


---Lua: number retval, number minval, number maxval, number midval = reaper.TrackFX_GetParamEx(MediaTrack track, integer fx, integer param)
function reaper.TrackFX_GetParamEx(track, fx, param)
end


---Lua: boolean retval, string buf = reaper.TrackFX_GetParamName(MediaTrack track, integer fx, integer param, string buf)
function reaper.TrackFX_GetParamName(track, fx, param, buf)
end


---Lua: number reaper.TrackFX_GetParamNormalized(MediaTrack track, integer fx, integer param)
function reaper.TrackFX_GetParamNormalized(track, fx, param)
end


---Lua: integer retval, optional number high32 = reaper.TrackFX_GetPinMappings(MediaTrack tr, integer fx, integer isoutput, integer pin)
---
---
---gets the effective channel mapping bitmask for a particular pin. high32OutOptional will be set to the high 32 bits
function reaper.TrackFX_GetPinMappings(tr, fx, isoutput, pin)
end


---Lua: boolean retval, string presetname = reaper.TrackFX_GetPreset(MediaTrack track, integer fx, string presetname)
---
---
---Get the name of the preset currently showing in the REAPER dropdown, or the full path to a factory preset file for VST3 plug-ins (.vstpreset). Returns false if the current FX parameters do not exactly match the preset (in other words, if the user loaded the preset but moved the knobs afterward). See TrackFX_SetPreset
---.
function reaper.TrackFX_GetPreset(track, fx, presetname)
end


---Lua: integer retval, number numberOfPresets = reaper.TrackFX_GetPresetIndex(MediaTrack track, integer fx)
---
---
---Returns current preset index, or -1 if error. numberOfPresetsOut will be set to total number of presets available. See TrackFX_SetPresetByIndex
function reaper.TrackFX_GetPresetIndex(track, fx)
end


---Lua: integer reaper.TrackFX_GetRecChainVisible(MediaTrack track)
---
---
---returns index of effect visible in record input chain, or -1 for chain hidden, or -2 for chain visible but no effect selected
function reaper.TrackFX_GetRecChainVisible(track)
end


---Lua: integer reaper.TrackFX_GetRecCount(MediaTrack track)
---
---
---returns count of record input FX. To access record input FX, use a FX indices [0x1000000..0x1000000+n). On the master track, this accesses monitoring FX rather than record input FX.
function reaper.TrackFX_GetRecCount(track)
end


---Lua: string fn = reaper.TrackFX_GetUserPresetFilename(MediaTrack track, integer fx, string fn)
function reaper.TrackFX_GetUserPresetFilename(track, fx, fn)
end


---Lua: boolean reaper.TrackFX_NavigatePresets(MediaTrack track, integer fx, integer presetmove)
---
---
---presetmove==1 activates the next preset, presetmove==-1 activates the previous preset, etc.
function reaper.TrackFX_NavigatePresets(track, fx, presetmove)
end


---Lua: reaper.TrackFX_SetEnabled(MediaTrack track, integer fx, boolean enabled)
---
---
---See TrackFX_GetEnabled
function reaper.TrackFX_SetEnabled(track, fx, enabled)
end


---Lua: boolean reaper.TrackFX_SetEQBandEnabled(MediaTrack track, integer fxidx, integer bandtype, integer bandidx, boolean enable)
---
---
---Enable or disable a ReaEQ band.
---
---Returns false if track/fxidx is not ReaEQ.
---
---Bandtype: 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
---
---Bandidx: 0=first band matching bandtype, 1=2nd band matching bandtype, etc.
---
---See TrackFX_GetEQ
---, TrackFX_GetEQParam
---, TrackFX_SetEQParam
---, TrackFX_GetEQBandEnabled
---.
function reaper.TrackFX_SetEQBandEnabled(track, fxidx, bandtype, bandidx, enable)
end


---Lua: boolean reaper.TrackFX_SetEQParam(MediaTrack track, integer fxidx, integer bandtype, integer bandidx, integer paramtype, number val, boolean isnorm)
---
---
---Returns false if track/fxidx is not ReaEQ. Targets a band matching bandtype.
---
---Bandtype: -1=master gain, 0=lhipass, 1=loshelf, 2=band, 3=notch, 4=hishelf, 5=lopass.
---
---Bandidx (ignored for master gain): 0=target first band matching bandtype, 1=target 2nd band matching bandtype, etc.
---
---Paramtype (ignored for master gain): 0=freq, 1=gain, 2=Q.
---
---See TrackFX_GetEQ
---, TrackFX_GetEQParam
---, TrackFX_GetEQBandEnabled
---, TrackFX_SetEQBandEnabled
---.
function reaper.TrackFX_SetEQParam(track, fxidx, bandtype, bandidx, paramtype, val, isnorm)
end


---Lua: boolean reaper.TrackFX_SetNamedConfigParm(MediaTrack track, integer fx, string parmname, string value)
---
---
---sets plug-in specific named configuration value (returns true on success)
function reaper.TrackFX_SetNamedConfigParm(track, fx, parmname, value)
end


---Lua: reaper.TrackFX_SetOffline(MediaTrack track, integer fx, boolean offline)
---
---
---See TrackFX_GetOffline
function reaper.TrackFX_SetOffline(track, fx, offline)
end


---Lua: reaper.TrackFX_SetOpen(MediaTrack track, integer fx, boolean open)
---
---
---Open this FX UI. See TrackFX_GetOpen
function reaper.TrackFX_SetOpen(track, fx, open)
end


---Lua: boolean reaper.TrackFX_SetParam(MediaTrack track, integer fx, integer param, number val)
function reaper.TrackFX_SetParam(track, fx, param, val)
end


---Lua: boolean reaper.TrackFX_SetParamNormalized(MediaTrack track, integer fx, integer param, number value)
function reaper.TrackFX_SetParamNormalized(track, fx, param, value)
end


---Lua: boolean reaper.TrackFX_SetPinMappings(MediaTrack tr, integer fx, integer isoutput, integer pin, integer low32bits, integer hi32bits)
---
---
---sets the channel mapping bitmask for a particular pin. returns false if unsupported (not all types of plug-ins support this capability)
function reaper.TrackFX_SetPinMappings(tr, fx, isoutput, pin, low32bits, hi32bits)
end


---Lua: boolean reaper.TrackFX_SetPreset(MediaTrack track, integer fx, string presetname)
---
---
---Activate a preset with the name shown in the REAPER dropdown. Full paths to .vstpreset files are also supported for VST3 plug-ins. See TrackFX_GetPreset
---.
function reaper.TrackFX_SetPreset(track, fx, presetname)
end


---Lua: boolean reaper.TrackFX_SetPresetByIndex(MediaTrack track, integer fx, integer idx)
---
---
---Sets the preset idx, or the factory preset (idx==-2), or the default user preset (idx==-1). Returns true on success. See TrackFX_GetPresetIndex
---.
function reaper.TrackFX_SetPresetByIndex(track, fx, idx)
end


---Lua: reaper.TrackFX_Show(MediaTrack track, integer index, integer showFlag)
---
---
---showflag=0 for hidechain, =1 for show chain(index valid), =2 for hide floating window(index valid), =3 for show floating window (index valid)
function reaper.TrackFX_Show(track, index, showFlag)
end


---Lua: reaper.TrackList_AdjustWindows(boolean isMinor)
function reaper.TrackList_AdjustWindows(isMinor)
end


---Lua: reaper.TrackList_UpdateAllExternalSurfaces()
function reaper.TrackList_UpdateAllExternalSurfaces()
end


---Lua: reaper.Undo_BeginBlock()
---
---
---call to start a new block
function reaper.Undo_BeginBlock()
end


---Lua: reaper.Undo_BeginBlock2(ReaProject proj)
---
---
---call to start a new block
function reaper.Undo_BeginBlock2(proj)
end


---Lua: string reaper.Undo_CanRedo2(ReaProject proj)
---
---
---returns string of next action,if able,NULL if not
function reaper.Undo_CanRedo2(proj)
end


---Lua: string reaper.Undo_CanUndo2(ReaProject proj)
---
---
---returns string of last action,if able,NULL if not
function reaper.Undo_CanUndo2(proj)
end


---Lua: integer reaper.Undo_DoRedo2(ReaProject proj)
---
---
---nonzero if success
function reaper.Undo_DoRedo2(proj)
end


---Lua: integer reaper.Undo_DoUndo2(ReaProject proj)
---
---
---nonzero if success
function reaper.Undo_DoUndo2(proj)
end


---Lua: reaper.Undo_EndBlock(string descchange, integer extraflags)
---
---
---call to end the block,with extra flags if any,and a description
function reaper.Undo_EndBlock(descchange, extraflags)
end


---Lua: reaper.Undo_EndBlock2(ReaProject proj, string descchange, integer extraflags)
---
---
---call to end the block,with extra flags if any,and a description
function reaper.Undo_EndBlock2(proj, descchange, extraflags)
end


---Lua: reaper.Undo_OnStateChange(string descchange)
---
---
---limited state change to items
function reaper.Undo_OnStateChange(descchange)
end


---Lua: reaper.Undo_OnStateChange2(ReaProject proj, string descchange)
---
---
---limited state change to items
function reaper.Undo_OnStateChange2(proj, descchange)
end


---Lua: reaper.Undo_OnStateChange_Item(ReaProject proj, string name, MediaItem item)
function reaper.Undo_OnStateChange_Item(proj, name, item)
end


---Lua: reaper.Undo_OnStateChangeEx(string descchange, integer whichStates, integer trackparm)
---
---
---trackparm=-1 by default,or if updating one fx chain,you can specify track index
function reaper.Undo_OnStateChangeEx(descchange, whichStates, trackparm)
end


---Lua: reaper.Undo_OnStateChangeEx2(ReaProject proj, string descchange, integer whichStates, integer trackparm)
---
---
---trackparm=-1 by default,or if updating one fx chain,you can specify track index
function reaper.Undo_OnStateChangeEx2(proj, descchange, whichStates, trackparm)
end


---Lua: reaper.UpdateArrange()
---
---
---Redraw the arrange view
function reaper.UpdateArrange()
end


---Lua: reaper.UpdateItemInProject(MediaItem item)
function reaper.UpdateItemInProject(item)
end


---Lua: reaper.UpdateTimeline()
---
---
---Redraw the arrange view and ruler
function reaper.UpdateTimeline()
end


---Lua: boolean reaper.ValidatePtr(identifier pointer, string ctypename)
---
---
---see ValidatePtr2
function reaper.ValidatePtr(pointer, ctypename)
end


---Lua: boolean reaper.ValidatePtr2(ReaProject proj, identifier pointer, string ctypename)
---
---
---Return true if the pointer is a valid object of the right type in proj (proj is ignored if pointer is itself a project). Supported types are: ReaProject*, MediaTrack*, MediaItem*, MediaItem_Take*, TrackEnvelope* and PCM_source*.
function reaper.ValidatePtr2(proj, pointer, ctypename)
end


---Lua: reaper.ViewPrefs(integer page, string pageByName)
---
---
---Opens the prefs to a page, use pageByName if page is 0.
function reaper.ViewPrefs(page, pageByName)
end


---Lua: BR_Envelope reaper.BR_EnvAlloc(TrackEnvelope envelope, boolean takeEnvelopesUseProjectTime)
---
---
---[BR] Allocate envelope object from track or take envelope pointer. Always call BR_EnvFree
--- when done to release the object and commit changes if needed.
---
--- takeEnvelopesUseProjectTime: take envelope points' positions are counted from take position, not project start time. If you want to work with project time instead, pass this as true.
---
---
---For further manipulation see BR_EnvCountPoints
---, BR_EnvDeletePoint
---, BR_EnvFind
---, BR_EnvFindNext
---, BR_EnvFindPrevious
---, BR_EnvGetParentTake
---, BR_EnvGetParentTrack
---, BR_EnvGetPoint
---, BR_EnvGetProperties
---, BR_EnvSetPoint
---, BR_EnvSetProperties
---, BR_EnvValueAtPos
---.
function reaper.BR_EnvAlloc(envelope, takeEnvelopesUseProjectTime)
end


---Lua: integer reaper.BR_EnvCountPoints(BR_Envelope envelope)
---
---
---[BR] Count envelope points in the envelope object allocated with BR_EnvAlloc
---.
function reaper.BR_EnvCountPoints(envelope)
end


---Lua: boolean reaper.BR_EnvDeletePoint(BR_Envelope envelope, integer id)
---
---
---[BR] Delete envelope point by index (zero-based) in the envelope object allocated with BR_EnvAlloc
---. Returns true on success.
function reaper.BR_EnvDeletePoint(envelope, id)
end


---Lua: integer reaper.BR_EnvFind(BR_Envelope envelope, number position, number delta)
---
---
---[BR] Find envelope point at time position in the envelope object allocated with BR_EnvAlloc
---. Pass delta > 0 to search surrounding range - in that case the closest point to position within delta will be searched for. Returns envelope point id (zero-based) on success or -1 on failure.
function reaper.BR_EnvFind(envelope, position, delta)
end


---Lua: integer reaper.BR_EnvFindNext(BR_Envelope envelope, number position)
---
---
---[BR] Find next envelope point after time position in the envelope object allocated with BR_EnvAlloc
---. Returns envelope point id (zero-based) on success or -1 on failure.
function reaper.BR_EnvFindNext(envelope, position)
end


---Lua: integer reaper.BR_EnvFindPrevious(BR_Envelope envelope, number position)
---
---
---[BR] Find previous envelope point before time position in the envelope object allocated with BR_EnvAlloc
---. Returns envelope point id (zero-based) on success or -1 on failure.
function reaper.BR_EnvFindPrevious(envelope, position)
end


---Lua: boolean reaper.BR_EnvFree(BR_Envelope envelope, boolean commit)
---
---
---[BR] Free envelope object allocated with BR_EnvAlloc
--- and commit changes if needed. Returns true if changes were committed successfully. Note that when envelope object wasn't modified nothing will get committed even if commit = true - in that case function returns false.
function reaper.BR_EnvFree(envelope, commit)
end


---Lua: MediaItem_Take reaper.BR_EnvGetParentTake(BR_Envelope envelope)
---
---
---[BR] If envelope object allocated with BR_EnvAlloc
--- is take envelope, returns parent media item take, otherwise NULL.
function reaper.BR_EnvGetParentTake(envelope)
end


---Lua: MediaItem reaper.BR_EnvGetParentTrack(BR_Envelope envelope)
---
---
---[BR] Get parent track of envelope object allocated with BR_EnvAlloc
---. If take envelope, returns NULL.
function reaper.BR_EnvGetParentTrack(envelope)
end


---Lua: boolean retval, number position, number value, number shape, boolean selected, number bezier = reaper.BR_EnvGetPoint(BR_Envelope envelope, integer id)
---
---
---[BR] Get envelope point by id (zero-based) from the envelope object allocated with BR_EnvAlloc
---. Returns true on success.
function reaper.BR_EnvGetPoint(envelope, id)
end


---Lua: boolean active, boolean visible, boolean armed, boolean inLane, number laneHeight, number defaultShape, number minValue, number maxValue, number centerValue, number type, boolean faderScaling = reaper.BR_EnvGetProperties(BR_Envelope envelope)
---
---
---[BR] Get envelope properties for the envelope object allocated with BR_EnvAlloc
---.
---
---
---active: true if envelope is active
---
---visible: true if envelope is visible
---
---armed: true if envelope is armed
---
---inLane: true if envelope has it's own envelope lane
---
---laneHeight: envelope lane override height. 0 for none, otherwise size in pixels
---
---defaultShape: default point shape: 0->Linear, 1->Square, 2->Slow start/end, 3->Fast start, 4->Fast end, 5->Bezier
---
---minValue: minimum envelope value
---
---maxValue: maximum envelope value
---
---type: envelope type: 0->Volume, 1->Volume (Pre-FX), 2->Pan, 3->Pan (Pre-FX), 4->Width, 5->Width (Pre-FX), 6->Mute, 7->Pitch, 8->Playrate, 9->Tempo map, 10->Parameter
---
---faderScaling: true if envelope uses fader scaling
function reaper.BR_EnvGetProperties(envelope)
end


---Lua: boolean reaper.BR_EnvSetPoint(BR_Envelope envelope, integer id, number position, number value, integer shape, boolean selected, number bezier)
---
---
---[BR] Set envelope point by id (zero-based) in the envelope object allocated with BR_EnvAlloc
---. To create point instead, pass id = -1. Note that if new point is inserted or existing point's time position is changed, points won't automatically get sorted. To do that, see BR_EnvSortPoints
---.
---
---Returns true on success.
function reaper.BR_EnvSetPoint(envelope, id, position, value, shape, selected, bezier)
end


---Lua: reaper.BR_EnvSetProperties(BR_Envelope envelope, boolean active, boolean visible, boolean armed, boolean inLane, integer laneHeight, integer defaultShape, boolean faderScaling)
---
---
---[BR] Set envelope properties for the envelope object allocated with BR_EnvAlloc
---. For parameter description see BR_EnvGetProperties
---.
function reaper.BR_EnvSetProperties(envelope, active, visible, armed, inLane, laneHeight, defaultShape, faderScaling)
end


---Lua: reaper.BR_EnvSortPoints(BR_Envelope envelope)
---
---
---[BR] Sort envelope points by position. The only reason to call this is if sorted points are explicitly needed after editing them with BR_EnvSetPoint
---. Note that you do not have to call this before doing BR_EnvFree
--- since it does handle unsorted points too.
function reaper.BR_EnvSortPoints(envelope)
end


---Lua: number reaper.BR_EnvValueAtPos(BR_Envelope envelope, number position)
---
---
---[BR] Get envelope value at time position for the envelope object allocated with BR_EnvAlloc
---.
function reaper.BR_EnvValueAtPos(envelope, position)
end


---Lua: number startTime, number endTime = reaper.BR_GetArrangeView(ReaProject proj)
---
---
---[BR] Deprecated, see GetSet_ArrangeView2
--- (REAPER v5.12pre4+) -- Get start and end time position of arrange view. To set arrange view instead, see BR_SetArrangeView
---.
function reaper.BR_GetArrangeView(proj)
end


---Lua: number reaper.BR_GetClosestGridDivision(number position)
---
---
---[BR] Get closest grid division to position. Note that this functions is different from SnapToGrid
--- in two regards. SnapToGrid() needs snap enabled to work and this one works always. Secondly, grid divisions are different from grid lines because some grid lines may be hidden due to zoom level - this function ignores grid line visibility and always searches for the closest grid division at given position. For more grid division functions, see BR_GetNextGridDivision
--- and BR_GetPrevGridDivision
---.
function reaper.BR_GetClosestGridDivision(position)
end


---Lua: string themePath, string themeName = reaper.BR_GetCurrentTheme()
---
---
---[BR] Get current theme information. themePathOut is set to full theme path and themeNameOut is set to theme name excluding any path info and extension
function reaper.BR_GetCurrentTheme()
end


---Lua: MediaItem reaper.BR_GetMediaItemByGUID(ReaProject proj, string guidStringIn)
---
---
---[BR] Get media item from GUID string. Note that the GUID must be enclosed in braces {}. To get item's GUID as a string, see BR_GetMediaItemGUID
---.
function reaper.BR_GetMediaItemByGUID(proj, guidStringIn)
end


---Lua: string guidString = reaper.BR_GetMediaItemGUID(MediaItem item)
---
---
---[BR] Get media item GUID as a string (guidStringOut_sz should be at least 64). To get media item back from GUID string, see BR_GetMediaItemByGUID
---.
function reaper.BR_GetMediaItemGUID(item)
end


---Lua: boolean retval, string image, number imageFlags = reaper.BR_GetMediaItemImageResource(MediaItem item)
---
---
---[BR] Get currently loaded image resource and it's flags for a given item. Returns false if there is no image resource set. To set image resource, see BR_SetMediaItemImageResource
---.
function reaper.BR_GetMediaItemImageResource(item)
end


---Lua: string guidString = reaper.BR_GetMediaItemTakeGUID(MediaItem_Take take)
---
---
---[BR] Get media item take GUID as a string (guidStringOut_sz should be at least 64). To get take from GUID string, see SNM_GetMediaItemTakeByGUID
---.
function reaper.BR_GetMediaItemTakeGUID(take)
end


---Lua: boolean retval, boolean section, number start, number length, number fade, boolean reverse = reaper.BR_GetMediaSourceProperties(MediaItem_Take take)
---
---
---[BR] Get take media source properties as they appear in Item properties
---. Returns false if take can't have them (MIDI items etc.).
---
---To set source properties, see BR_SetMediaSourceProperties
---.
function reaper.BR_GetMediaSourceProperties(take)
end


---Lua: MediaTrack reaper.BR_GetMediaTrackByGUID(ReaProject proj, string guidStringIn)
---
---
---[BR] Get media track from GUID string. Note that the GUID must be enclosed in braces {}. To get track's GUID as a string, see BR_GetMediaTrackGUID
---.
function reaper.BR_GetMediaTrackByGUID(proj, guidStringIn)
end


---Lua: integer reaper.BR_GetMediaTrackFreezeCount(MediaTrack track)
---
---
---[BR] Get media track freeze count (if track isn't frozen at all, returns 0).
function reaper.BR_GetMediaTrackFreezeCount(track)
end


---Lua: string guidString = reaper.BR_GetMediaTrackGUID(MediaTrack track)
---
---
---[BR] Get media track GUID as a string (guidStringOut_sz should be at least 64). To get media track back from GUID string, see BR_GetMediaTrackByGUID
---.
function reaper.BR_GetMediaTrackGUID(track)
end


---Lua: string mcpLayoutName, string tcpLayoutName = reaper.BR_GetMediaTrackLayouts(MediaTrack track)
---
---
---[BR] Deprecated, see GetSetMediaTrackInfo
--- (REAPER v5.02+). Get media track layouts for MCP and TCP. Empty string ("") means that layout is set to the default layout. To set media track layouts, see BR_SetMediaTrackLayouts
---.
function reaper.BR_GetMediaTrackLayouts(track)
end


---Lua: TrackEnvelope reaper.BR_GetMediaTrackSendInfo_Envelope(MediaTrack track, integer category, integer sendidx, integer envelopeType)
---
---
---[BR] Get track envelope for send/receive/hardware output.
---
---
---category is <0 for receives, 0=sends, >0 for hardware outputs
---
---sendidx is zero-based (see GetTrackNumSends
--- to count track sends/receives/hardware outputs)
---
---envelopeType determines which envelope is returned (0=volume, 1=pan, 2=mute)
---
---
---Note: To get or set other send attributes, see BR_GetSetTrackSendInfo
--- and BR_GetMediaTrackSendInfo_Track
---.
function reaper.BR_GetMediaTrackSendInfo_Envelope(track, category, sendidx, envelopeType)
end


---Lua: MediaTrack reaper.BR_GetMediaTrackSendInfo_Track(MediaTrack track, integer category, integer sendidx, integer trackType)
---
---
---[BR] Get source or destination media track for send/receive.
---
---
---category is <0 for receives, 0=sends
---
---sendidx is zero-based (see GetTrackNumSends
--- to count track sends/receives)
---
---trackType determines which track is returned (0=source track, 1=destination track)
---
---
---Note: To get or set other send attributes, see BR_GetSetTrackSendInfo
--- and BR_GetMediaTrackSendInfo_Envelope
---.
function reaper.BR_GetMediaTrackSendInfo_Track(track, category, sendidx, trackType)
end


---Lua: number reaper.BR_GetMidiSourceLenPPQ(MediaItem_Take take)
---
---
---[BR] Get MIDI take source length in PPQ. In case the take isn't MIDI, return value will be -1.
function reaper.BR_GetMidiSourceLenPPQ(take)
end


---Lua: boolean retval, string guidString = reaper.BR_GetMidiTakePoolGUID(MediaItem_Take take)
---
---
---[BR] Get MIDI take pool GUID as a string (guidStringOut_sz should be at least 64). Returns true if take is pooled.
function reaper.BR_GetMidiTakePoolGUID(take)
end


---Lua: boolean retval, boolean ignoreProjTempo, number bpm, number num, number den = reaper.BR_GetMidiTakeTempoInfo(MediaItem_Take take)
---
---
---[BR] Get "ignore project tempo" information for MIDI take. Returns true if take can ignore project tempo (no matter if it's actually ignored), otherwise false.
function reaper.BR_GetMidiTakeTempoInfo(take)
end


---Lua: string window, string segment, string details = reaper.BR_GetMouseCursorContext()
---
---
---[BR] Get mouse cursor context. Each parameter returns information in a form of string as specified in the table below.
---
---
---To get more info on stuff that was found under mouse cursor see BR_GetMouseCursorContext_Envelope
---, BR_GetMouseCursorContext_Item
---, BR_GetMouseCursorContext_MIDI
---, BR_GetMouseCursorContext_Position
---, BR_GetMouseCursorContext_Take
---, BR_GetMouseCursorContext_Track
---
---Window Segment Details  unknown       ""          ""                                                             ruler         region_lane   ""                                                              marker_lane   ""                                                              tempo_lane    ""                                                              timeline      ""                                                             transport     ""          ""                                                             tcp           track         ""                                                              envelope      ""                                                              empty         ""                                                             mcp           track         ""                                                              empty         ""                                                             arrange       track         empty,item, item_stretch_marker,env_point, env_segment    envelope      empty, env_point, env_segment                                     empty         ""                                                             midi_editor   unknown       ""                                                              ruler         ""                                                              piano         ""                                                              notes         ""                                                              cc_lane       cc_selector, cc_lane
function reaper.BR_GetMouseCursorContext()
end


---Lua: TrackEnvelope retval, boolean takeEnvelope = reaper.BR_GetMouseCursorContext_Envelope()
---
---
---[BR] Returns envelope that was captured with the last call to BR_GetMouseCursorContext
---. In case the envelope belongs to take, takeEnvelope will be true.
function reaper.BR_GetMouseCursorContext_Envelope()
end


---Lua: MediaItem reaper.BR_GetMouseCursorContext_Item()
---
---
---[BR] Returns item under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
---. Note that the function will return item even if mouse cursor is over some other track lane element like stretch marker or envelope. This enables for easier identification of items when you want to ignore elements within the item.
function reaper.BR_GetMouseCursorContext_Item()
end


---Lua: identifier retval, boolean inlineEditor, number noteRow, number ccLane, number ccLaneVal, number ccLaneId = reaper.BR_GetMouseCursorContext_MIDI()
---
---
---[BR] Returns midi editor under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
---.
---
---
---inlineEditor: if mouse was captured in inline MIDI editor, this will be true (consequentially, returned MIDI editor will be NULL)
---
---noteRow: note row or piano key under mouse cursor (0-127)
---
---ccLane: CC lane under mouse cursor (CC0-127=CC, 0x100|(0-31)=14-bit CC, 0x200=velocity, 0x201=pitch, 0x202=program, 0x203=channel pressure, 0x204=bank/program select, 0x205=text, 0x206=sysex, 0x207=off velocity)
---
---ccLaneVal: value in CC lane under mouse cursor (0-127 or 0-16383)
---
---ccLaneId: lane position, counting from the top (0 based)
---
---
---Note: due to API limitations, if mouse is over inline MIDI editor with some note rows hidden, noteRow will be -1
function reaper.BR_GetMouseCursorContext_MIDI()
end


---Lua: number reaper.BR_GetMouseCursorContext_Position()
---
---
---[BR] Returns project time position in arrange/ruler/midi editor that was captured with the last call to BR_GetMouseCursorContext
---.
function reaper.BR_GetMouseCursorContext_Position()
end


---Lua: integer reaper.BR_GetMouseCursorContext_StretchMarker()
---
---
---[BR] Returns id of a stretch marker under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
---.
function reaper.BR_GetMouseCursorContext_StretchMarker()
end


---Lua: MediaItem_Take reaper.BR_GetMouseCursorContext_Take()
---
---
---[BR] Returns take under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
---.
function reaper.BR_GetMouseCursorContext_Take()
end


---Lua: MediaTrack reaper.BR_GetMouseCursorContext_Track()
---
---
---[BR] Returns track under mouse cursor that was captured with the last call to BR_GetMouseCursorContext
---.
function reaper.BR_GetMouseCursorContext_Track()
end


---Lua: number reaper.BR_GetNextGridDivision(number position)
---
---
---[BR] Get next grid division after the time position. For more grid divisions function, see BR_GetClosestGridDivision
--- and BR_GetPrevGridDivision
---.
function reaper.BR_GetNextGridDivision(position)
end


---Lua: number reaper.BR_GetPrevGridDivision(number position)
---
---
---[BR] Get previous grid division before the time position. For more grid division functions, see BR_GetClosestGridDivision
--- and BR_GetNextGridDivision
---.
function reaper.BR_GetPrevGridDivision(position)
end


---Lua: number reaper.BR_GetSetTrackSendInfo(MediaTrack track, integer category, integer sendidx, string parmname, boolean setNewValue, number newValue)
---
---
---[BR] Get or set send attributes.
---
---
---category is <0 for receives, 0=sends, >0 for hardware outputs
---
---sendidx is zero-based (see GetTrackNumSends
--- to count track sends/receives/hardware outputs)
---
---To set attribute, pass setNewValue as true
---
---
---List of possible parameters:
---
---B_MUTE : send mute state (1.0 if muted, otherwise 0.0)
---
---B_PHASE : send phase state (1.0 if phase is inverted, otherwise 0.0)
---
---B_MONO : send mono state (1.0 if send is set to mono, otherwise 0.0)
---
---D_VOL : send volume (1.0=+0dB etc...)
---
---D_PAN : send pan (-1.0=100%L, 0=center, 1.0=100%R)
---
---D_PANLAW : send pan law (1.0=+0.0db, 0.5=-6dB, -1.0=project default etc...)
---
---I_SENDMODE : send mode (0=post-fader, 1=pre-fx, 2=post-fx(deprecated), 3=post-fx)
---
---I_SRCCHAN : audio source starting channel index or -1 if audio send is disabled (&1024=mono...note that in that case, when reading index, you should do (index XOR 1024) to get starting channel index)
---
---I_DSTCHAN : audio destination starting channel index (&1024=mono (and in case of hardware output &512=rearoute)...note that in that case, when reading index, you should do (index XOR (1024 OR 512)) to get starting channel index)
---
---I_MIDI_SRCCHAN : source MIDI channel, -1 if MIDI send is disabled (0=all, 1-16)
---
---I_MIDI_DSTCHAN : destination MIDI channel, -1 if MIDI send is disabled (0=original, 1-16)
---
---I_MIDI_SRCBUS : source MIDI bus, -1 if MIDI send is disabled (0=all, otherwise bus index)
---
---I_MIDI_DSTBUS : receive MIDI bus, -1 if MIDI send is disabled (0=all, otherwise bus index)
---
---I_MIDI_LINK_VOLPAN : link volume/pan controls to MIDI
---
---
---Note: To get or set other send attributes, see BR_GetMediaTrackSendInfo_Envelope
--- and BR_GetMediaTrackSendInfo_Track
---.
function reaper.BR_GetSetTrackSendInfo(track, category, sendidx, parmname, setNewValue, newValue)
end


---Lua: integer reaper.BR_GetTakeFXCount(MediaItem_Take take)
---
---
---[BR] Returns FX count for supplied take
function reaper.BR_GetTakeFXCount(take)
end


---Lua: boolean reaper.BR_IsMidiOpenInInlineEditor(MediaItem_Take take)
---
---
---[SWS] Check if take has MIDI inline editor open and returns true or false.
function reaper.BR_IsMidiOpenInInlineEditor(take)
end


---Lua: boolean retval, boolean inProjectMidi = reaper.BR_IsTakeMidi(MediaItem_Take take)
---
---
---[BR] Check if take is MIDI take, in case MIDI take is in-project MIDI source data, inProjectMidiOut will be true, otherwise false.
function reaper.BR_IsTakeMidi(take)
end


---Lua: MediaItem retval, number position = reaper.BR_ItemAtMouseCursor()
---
---
---[BR] Get media item under mouse cursor. Position is mouse cursor position in arrange.
function reaper.BR_ItemAtMouseCursor()
end


---Lua: boolean reaper.BR_MIDI_CCLaneRemove(HWND midiEditor, integer laneId)
---
---
---[BR] Remove CC lane in midi editor. Returns true on success
function reaper.BR_MIDI_CCLaneRemove(midiEditor, laneId)
end


---Lua: boolean reaper.BR_MIDI_CCLaneReplace(HWND midiEditor, integer laneId, integer newCC)
---
---
---[BR] Replace CC lane in midi editor. Returns true on success.
---
---Valid CC lanes: CC0-127=CC, 0x100|(0-31)=14-bit CC, 0x200=velocity, 0x201=pitch, 0x202=program, 0x203=channel pressure, 0x204=bank/program select, 0x205=text, 0x206=sysex, 0x207
function reaper.BR_MIDI_CCLaneReplace(midiEditor, laneId, newCC)
end


---Lua: number reaper.BR_PositionAtMouseCursor(boolean checkRuler)
---
---
---[BR] Get position at mouse cursor. To check ruler along with arrange, pass checkRuler=true. Returns -1 if cursor is not over arrange/ruler.
function reaper.BR_PositionAtMouseCursor(checkRuler)
end


---Lua: reaper.BR_SetArrangeView(ReaProject proj, number startTime, number endTime)
---
---
---[BR] Deprecated, see GetSet_ArrangeView2
--- (REAPER v5.12pre4+) -- Set start and end time position of arrange view. To get arrange view instead, see BR_GetArrangeView
---.
function reaper.BR_SetArrangeView(proj, startTime, endTime)
end


---Lua: boolean reaper.BR_SetItemEdges(MediaItem item, number startTime, number endTime)
---
---
---[BR] Set item start and end edges' position - returns true in case of any changes
function reaper.BR_SetItemEdges(item, startTime, endTime)
end


---Lua: reaper.BR_SetMediaItemImageResource(MediaItem item, string imageIn, integer imageFlags)
---
---
---[BR] Set image resource and it's flags for a given item. To clear current image resource, pass imageIn as . To get image resource, see BR_GetMediaItemImageResource
---.
function reaper.BR_SetMediaItemImageResource(item, imageIn, imageFlags)
end


---Lua: boolean reaper.BR_SetMediaSourceProperties(MediaItem_Take take, boolean section, number start, number length, number fade, boolean reverse)
---
---
---[BR] Set take media source properties. Returns false if take can't have them (MIDI items etc.). Section parameters have to be valid only when passing section=true.
---
---To get source properties, see BR_GetMediaSourceProperties
---.
function reaper.BR_SetMediaSourceProperties(take, section, start, length, fade, reverse)
end


---Lua: boolean reaper.BR_SetMediaTrackLayouts(MediaTrack track, string mcpLayoutNameIn, string tcpLayoutNameIn)
---
---
---[BR] Deprecated, see GetSetMediaTrackInfo
--- (REAPER v5.02+). Set media track layouts for MCP and TCP. To set default layout, pass empty string ("") as layout name. In case layouts were successfully set, returns true (if layouts are already set to supplied layout names, it will return false since no changes were made).
---
---To get media track layouts, see BR_GetMediaTrackLayouts
---.
function reaper.BR_SetMediaTrackLayouts(track, mcpLayoutNameIn, tcpLayoutNameIn)
end


---Lua: boolean reaper.BR_SetMidiTakeTempoInfo(MediaItem_Take take, boolean ignoreProjTempo, number bpm, integer num, integer den)
---
---
---[BR] Set "ignore project tempo" information for MIDI take. Returns true in case the take was successfully updated.
function reaper.BR_SetMidiTakeTempoInfo(take, ignoreProjTempo, bpm, num, den)
end


---Lua: boolean reaper.BR_SetTakeSourceFromFile(MediaItem_Take take, string filenameIn, boolean inProjectData)
---
---
---[BR] Set new take source from file. To import MIDI file as in-project source data pass inProjectData=true. Returns false if failed.
---
---Any take source properties from the previous source will be lost - to preserve them, see BR_SetTakeSourceFromFile2
---.
---
---Note: To set source from existing take, see SNM_GetSetSourceState2
---.
function reaper.BR_SetTakeSourceFromFile(take, filenameIn, inProjectData)
end


---Lua: boolean reaper.BR_SetTakeSourceFromFile2(MediaItem_Take take, string filenameIn, boolean inProjectData, boolean keepSourceProperties)
---
---
---[BR] Differs from BR_SetTakeSourceFromFile
--- only that it can also preserve existing take media source properties.
function reaper.BR_SetTakeSourceFromFile2(take, filenameIn, inProjectData, keepSourceProperties)
end


---Lua: MediaItem_Take retval, number position = reaper.BR_TakeAtMouseCursor()
---
---
---[BR] Get take under mouse cursor. Position is mouse cursor position in arrange.
function reaper.BR_TakeAtMouseCursor()
end


---Lua: MediaTrack retval, number context, number position = reaper.BR_TrackAtMouseCursor()
---
---
---[BR] Get track under mouse cursor.
---
---Context signifies where the track was found: 0 = TCP, 1 = MCP, 2 = Arrange.
---
---Position will hold mouse cursor position in arrange if applicable.
function reaper.BR_TrackAtMouseCursor()
end


---Lua: boolean retval, string  name = reaper.BR_TrackFX_GetFXModuleName(MediaTrack track, integer fx)
---
---
---[BR] Get the exact name (like effect.dll, effect.vst3, etc...) of an FX.
function reaper.BR_TrackFX_GetFXModuleName(track, fx)
end


---Lua: integer retval, string string = reaper.BR_Win32_GetPrivateProfileString(string sectionName, string keyName, string defaultString, string filePath)
---
---
---[BR] Equivalent to win32 API GetPrivateProfileString(). For example, you can use this to get values from REAPER.ini
function reaper.BR_Win32_GetPrivateProfileString(sectionName, keyName, defaultString, filePath)
end


---Lua: integer reaper.BR_Win32_ShellExecute(string operation, string file, string parameters, string directory, integer showFlags)
---
---
---[BR] Equivalent to win32 API ShellExecute() with HWND set to main window
function reaper.BR_Win32_ShellExecute(operation, file, parameters, directory, showFlags)
end


---Lua: boolean reaper.BR_Win32_WritePrivateProfileString(string sectionName, string keyName, string value, string filePath)
---
---
---[BR] Equivalent to win32 API WritePrivateProfileString(). For example, you can use this to write to REAPER.ini
function reaper.BR_Win32_WritePrivateProfileString(sectionName, keyName, value, filePath)
end


---Lua: string buf = reaper.CF_GetClipboard(string buf)
---
---
---Read the contents of the system clipboard (limited to 1023 characters in Lua).
function reaper.CF_GetClipboard(buf)
end


---Lua: string reaper.CF_GetClipboardBig(WDL_FastString output)
---
---
---Read the contents of the system clipboard. See SNM_CreateFastString
--- and SNM_DeleteFastString
---.
function reaper.CF_GetClipboardBig(output)
end


---Lua: reaper.CF_SetClipboard(string str)
---
---
---Write the given string into the system clipboard.
function reaper.CF_SetClipboard(str)
end


---Lua: RprMidiNote reaper.FNG_AddMidiNote(RprMidiTake midiTake)
---
---
---[FNG] Add MIDI note to MIDI take
function reaper.FNG_AddMidiNote(midiTake)
end


---Lua: RprMidiTake reaper.FNG_AllocMidiTake(MediaItem_Take take)
---
---
---[FNG] Allocate a RprMidiTake from a take pointer. Returns a NULL pointer if the take is not an in-project MIDI take
function reaper.FNG_AllocMidiTake(take)
end


---Lua: integer reaper.FNG_CountMidiNotes(RprMidiTake midiTake)
---
---
---[FNG] Count of how many MIDI notes are in the MIDI take
function reaper.FNG_CountMidiNotes(midiTake)
end


---Lua: reaper.FNG_FreeMidiTake(RprMidiTake midiTake)
---
---
---[FNG] Commit changes to MIDI take and free allocated memory
function reaper.FNG_FreeMidiTake(midiTake)
end


---Lua: RprMidiNote reaper.FNG_GetMidiNote(RprMidiTake midiTake, integer index)
---
---
---[FNG] Get a MIDI note from a MIDI take at specified index
function reaper.FNG_GetMidiNote(midiTake, index)
end


---Lua: integer reaper.FNG_GetMidiNoteIntProperty(RprMidiNote midiNote, string property)
---
---
---[FNG] Get MIDI note property
function reaper.FNG_GetMidiNoteIntProperty(midiNote, property)
end


---Lua: reaper.FNG_SetMidiNoteIntProperty(RprMidiNote midiNote, string property, integer value)
---
---
---[FNG] Set MIDI note property
function reaper.FNG_SetMidiNoteIntProperty(midiNote, property, value)
end


---Lua: boolean retval, number lufsIntegrated, number range, number  truePeak, number truePeakPos, number shortTermMax, number momentaryMax = reaper.NF_AnalyzeTakeLoudness(MediaItem_Take take, boolean analyzeTruePeak)
---
---
---Full loudness analysis. retval: returns true on successful analysis, false on MIDI take or when analysis failed for some reason. analyzeTruePeak=true: Also do true peak analysis. Returns true peak value and true peak position which can be jumped to with SetEditCurPos(). Considerably slower than without true peak analysis (since it uses oversampling). Note: Short term uses a time window of 3 sec. for calculation. So for items shorter than this shortTermMaxOut can't be calculated. Momentary uses a time window of 0.4 sec.
function reaper.NF_AnalyzeTakeLoudness(take, analyzeTruePeak)
end


---Lua: boolean retval, number lufsIntegrated, number range, number  truePeak, number truePeakPos, number shortTermMax, number momentaryMax, number shortTermMaxPos, number momentaryMaxPos = reaper.NF_AnalyzeTakeLoudness2(MediaItem_Take take, boolean analyzeTruePeak)
---
---
---Same as NF_AnalyzeTakeLoudness
--- but additionally returns shortTermMaxPos and momentaryMaxPos which can be jumped to with SetEditCurPos(). Note: shortTermMaxPos and momentaryMaxPos actaully indicate the beginning of time  intervalls
---, (3 sec. and 0.4 sec. resp.).
function reaper.NF_AnalyzeTakeLoudness2(take, analyzeTruePeak)
end


---Lua: boolean retval, number lufsIntegrated = reaper.NF_AnalyzeTakeLoudness_IntegratedOnly(MediaItem_Take take)
---
---
---Does LUFS integrated analysis only. Faster than full loudness analysis (NF_AnalyzeTakeLoudness
---) . Use this if only LUFS integrated is required.
function reaper.NF_AnalyzeTakeLoudness_IntegratedOnly(take)
end


---Lua: number reaper.NF_GetMediaItemAverageRMS(MediaItem item)
---
---
---Returns the average overall (non-windowed) RMS level of active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX.
---
--- Returns -150.0 if MIDI take or empty item.
function reaper.NF_GetMediaItemAverageRMS(item)
end


---Lua: number reaper.NF_GetMediaItemMaxPeak(MediaItem item)
---
---
---Returns the greatest max. peak value of all active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX.
---
--- Returns -150.0 if MIDI take or empty item.
function reaper.NF_GetMediaItemMaxPeak(item)
end


---Lua: number reaper.NF_GetMediaItemPeakRMS_NonWindowed(MediaItem item)
---
---
---Returns the greatest overall (non-windowed) RMS peak level of all active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX.
---
--- Returns -150.0 if MIDI take or empty item.
function reaper.NF_GetMediaItemPeakRMS_NonWindowed(item)
end


---Lua: number reaper.NF_GetMediaItemPeakRMS_Windowed(MediaItem item)
---
---
---Returns the average RMS peak level of all active channels of an audio item active take, post item gain, post take volume envelope, post-fade, pre fader, pre item FX.
---
--- Obeys 'Window size for peak RMS' setting in 'SWS: Set RMS analysis/normalize options' for calculation. Returns -150.0 if MIDI take or empty item.
function reaper.NF_GetMediaItemPeakRMS_Windowed(item)
end


---Lua: boolean reaper.ReaPack_AboutInstalledPackage(PackageEntry entry)
---
---
---Show the about dialog of the given package entry.
---
---The repository index is downloaded asynchronously if the cached copy doesn't exist or is older than one week.
function reaper.ReaPack_AboutInstalledPackage(entry)
end


---Lua: boolean reaper.ReaPack_AboutRepository(string repoName)
---
---
---Show the about dialog of the given repository. Returns true if the repository exists in the user configuration.
---
---The repository index is downloaded asynchronously if the cached copy doesn't exist or is older than one week.
function reaper.ReaPack_AboutRepository(repoName)
end


---Lua: boolean retval, string error = reaper.ReaPack_AddSetRepository(string name, string url, boolean enable, integer autoInstall)
---
---
---Add or modify a repository. Set url to nullptr (or empty string in Lua) to keep the existing URL. Call ReaPack_ProcessQueue(true)
--- when done to process the new list and update the GUI.
---
---
---autoInstall: usually set to 2 (obey user setting).
function reaper.ReaPack_AddSetRepository(name, url, enable, autoInstall)
end


---Lua: reaper.ReaPack_BrowsePackages(string filter)
---
---
---Opens the package browser with the given filter string.
function reaper.ReaPack_BrowsePackages(filter)
end


---Lua: integer retval, string error = reaper.ReaPack_CompareVersions(string ver1, string ver2)
---
---
---Returns 0 if both versions are equal, a positive value if ver1 is higher than ver2 and a negative value otherwise.
function reaper.ReaPack_CompareVersions(ver1, ver2)
end


---Lua: boolean retval, string path, number sections, number type = reaper.ReaPack_EnumOwnedFiles(PackageEntry entry, integer index)
---
---
---Enumerate the files owned by the given package. Returns false when there is no more data.
---
---
---sections: 0=not in action list, &1=main, &2=midi editor, &4=midi inline editor
---
---type: see ReaPack_GetEntryInfo
---.
function reaper.ReaPack_EnumOwnedFiles(entry, index)
end


---Lua: boolean reaper.ReaPack_FreeEntry(PackageEntry entry)
---
---
---Free resources allocated for the given package entry.
function reaper.ReaPack_FreeEntry(entry)
end


---Lua: boolean retval, string repo, string cat, string pkg, string desc, number type, string ver, string author, boolean pinned, number fileCount = reaper.ReaPack_GetEntryInfo(PackageEntry entry)
---
---
---Get the repository name, category, package name, package description, package type, the currently installed version, author name, pinned status and how many files are owned by the given package entry.
---
---
---type: 1=script, 2=extension, 3=effect, 4=data, 5=theme, 6=langpack, 7=webinterface
function reaper.ReaPack_GetEntryInfo(entry)
end


---Lua: PackageEntry retval, string error = reaper.ReaPack_GetOwner(string fn)
---
---
---Returns the package entry owning the given file.
---
---Delete the returned object from memory after use with ReaPack_FreeEntry
---.
function reaper.ReaPack_GetOwner(fn)
end


---Lua: boolean retval, string url, boolean enabled, number autoInstall = reaper.ReaPack_GetRepositoryInfo(string name)
---
---
---Get the infos of the given repository.
---
---
---autoInstall: 0=manual, 1=when sychronizing, 2=obey user setting
function reaper.ReaPack_GetRepositoryInfo(name)
end


---Lua: reaper.ReaPack_ProcessQueue(boolean refreshUI)
---
---
---Run pending operations and save the configuration file. If refreshUI is true the browser and manager windows are guaranteed to be refreshed (otherwise it depends on which operations are in the queue).
function reaper.ReaPack_ProcessQueue(refreshUI)
end


---Lua: reaper.SN_FocusMIDIEditor()
---
---
---Focuses the active/open MIDI editor.
function reaper.SN_FocusMIDIEditor()
end


---Lua: boolean reaper.SNM_AddReceive(MediaTrack src, MediaTrack dest, integer type)
---
---
---[S&M] Deprecated, see CreateTrackSend
--- (v5.15pre1+). Adds a receive. Returns false if nothing updated.
---
---type -1=Default type (user preferences), 0=Post-Fader (Post-Pan), 1=Pre-FX, 2=deprecated, 3=Pre-Fader (Post-FX).
---
---Note: obeys default sends preferences, supports frozen tracks, etc..
function reaper.SNM_AddReceive(src, dest, type)
end


---Lua: boolean reaper.SNM_AddTCPFXParm(MediaTrack tr, integer fxId, integer prmId)
---
---
---[S&M] Add an FX parameter knob in the TCP. Returns false if nothing updated (invalid parameters, knob already present, etc..)
function reaper.SNM_AddTCPFXParm(tr, fxId, prmId)
end


---Lua: WDL_FastString reaper.SNM_CreateFastString(string str)
---
---
---[S&M] Instantiates a new "fast string". You must delete this string, see SNM_DeleteFastString
---.
function reaper.SNM_CreateFastString(str)
end


---Lua: reaper.SNM_DeleteFastString(WDL_FastString str)
---
---
---[S&M] Deletes a "fast string" instance.
function reaper.SNM_DeleteFastString(str)
end


---Lua: number reaper.SNM_GetDoubleConfigVar(string varname, number errvalue)
---
---
---[S&M] Returns a double preference (look in project prefs first, then in general prefs). Returns errvalue if failed (e.g. varname not found).
function reaper.SNM_GetDoubleConfigVar(varname, errvalue)
end


---Lua: string reaper.SNM_GetFastString(WDL_FastString str)
---
---
---[S&M] Gets the "fast string" content.
function reaper.SNM_GetFastString(str)
end


---Lua: integer reaper.SNM_GetFastStringLength(WDL_FastString str)
---
---
---[S&M] Gets the "fast string" length.
function reaper.SNM_GetFastStringLength(str)
end


---Lua: integer reaper.SNM_GetIntConfigVar(string varname, integer errvalue)
---
---
---[S&M] Returns an integer preference (look in project prefs first, then in general prefs). Returns errvalue if failed (e.g. varname not found).
function reaper.SNM_GetIntConfigVar(varname, errvalue)
end


---Lua: MediaItem_Take reaper.SNM_GetMediaItemTakeByGUID(ReaProject project, string guid)
---
---
---[S&M] Gets a take by GUID as string. The GUID must be enclosed in braces {}. To get take GUID as string, see BR_GetMediaItemTakeGUID
function reaper.SNM_GetMediaItemTakeByGUID(project, guid)
end


---Lua: boolean reaper.SNM_GetProjectMarkerName(ReaProject proj, integer num, boolean isrgnWDL_FastString name)
---
---
---[S&M] Gets a marker/region name. Returns true if marker/region found.
function reaper.SNM_GetProjectMarkerName(proj, num, name)
end


---Lua: boolean reaper.SNM_GetSetObjectState(identifier objWDL_FastString state, boolean setnewvalue, boolean wantminimalstate)
---
---
---[S&M] Gets or sets the state of a track, an item or an envelope. The state chunk size is unlimited. Returns false if failed.
---
---When getting a track state (and when you are not interested in FX data), you can use wantminimalstate=true to radically reduce the length of the state. Do not set such minimal states back though, this is for read-only applications!
---
---Note: unlike the native GetSetObjectState, calling to FreeHeapPtr() is not required.
function reaper.SNM_GetSetObjectState(state, setnewvalue, wantminimalstate)
end


---Lua: boolean reaper.SNM_GetSetSourceState(MediaItem item, integer takeidxWDL_FastString state, boolean setnewvalue)
---
---
---[S&M] Gets or sets a take source state. Returns false if failed. Use takeidx=-1 to get/alter the active take.
---
---Note: this function does not use a MediaItem_Take* param in order to manage empty takes (i.e. takes with MediaItem_Take*==NULL), see SNM_GetSetSourceState2
---.
function reaper.SNM_GetSetSourceState(item, state, setnewvalue)
end


---Lua: boolean reaper.SNM_GetSetSourceState2(MediaItem_Take takeWDL_FastString state, boolean setnewvalue)
---
---
---[S&M] Gets or sets a take source state. Returns false if failed.
---
---Note: this function cannot deal with empty takes, see SNM_GetSetSourceState
---.
function reaper.SNM_GetSetSourceState2(state, setnewvalue)
end


---Lua: boolean reaper.SNM_GetSourceType(MediaItem_Take takeWDL_FastString type)
---
---
---[S&M] Gets the source type of a take. Returns false if failed (e.g. take with empty source, etc..)
function reaper.SNM_GetSourceType(type)
end


---Lua: boolean reaper.SNM_MoveOrRemoveTrackFX(MediaTrack tr, integer fxId, integer what)
---
---
---[S&M] Move or removes a track FX. Returns true if tr has been updated.
---
---fxId: fx index in chain or -1 for the selected fx. what: 0 to remove, -1 to move fx up in chain, 1 to move fx down in chain.
function reaper.SNM_MoveOrRemoveTrackFX(tr, fxId, what)
end


---Lua: boolean retval, string tagval = reaper.SNM_ReadMediaFileTag(string fn, string tag, string tagval)
---
---
---[S&M] Reads a media file tag. Supported tags: "artist", "album", "genre", "comment", "title", or "year". Returns false if tag was not found. See SNM_TagMediaFile
---.
function reaper.SNM_ReadMediaFileTag(fn, tag, tagval)
end


---Lua: boolean reaper.SNM_RemoveReceive(MediaTrack tr, integer rcvidx)
---
---
---[S&M] Deprecated, see RemoveTrackSend
--- (v5.15pre1+). Removes a receive. Returns false if nothing updated.
function reaper.SNM_RemoveReceive(tr, rcvidx)
end


---Lua: boolean reaper.SNM_RemoveReceivesFrom(MediaTrack tr, MediaTrack srctr)
---
---
---[S&M] Removes all receives from srctr. Returns false if nothing updated.
function reaper.SNM_RemoveReceivesFrom(tr, srctr)
end


---Lua: integer reaper.SNM_SelectResourceBookmark(string name)
---
---
---[S&M] Select a bookmark of the Resources window. Returns the related bookmark id (or -1 if failed).
function reaper.SNM_SelectResourceBookmark(name)
end


---Lua: boolean reaper.SNM_SetDoubleConfigVar(string varname, number newvalue)
---
---
---[S&M] Sets a double preference (look in project prefs first, then in general prefs). Returns false if failed (e.g. varname not found).
function reaper.SNM_SetDoubleConfigVar(varname, newvalue)
end


---Lua: WDL_FastString reaper.SNM_SetFastString(WDL_FastString str, string newstr)
---
---
---[S&M] Sets the "fast string" content. Returns str for facility.
function reaper.SNM_SetFastString(str, newstr)
end


---Lua: boolean reaper.SNM_SetIntConfigVar(string varname, integer newvalue)
---
---
---[S&M] Sets an integer preference (look in project prefs first, then in general prefs). Returns false if failed (e.g. varname not found).
function reaper.SNM_SetIntConfigVar(varname, newvalue)
end


---Lua: boolean reaper.SNM_SetProjectMarker(ReaProject proj, integer num, boolean isrgn, number pos, number rgnend, string name, integer color)
---
---
---[S&M] Deprecated, see SetProjectMarker4
--- -- Same function as SetProjectMarker3() except it can set empty names "".
function reaper.SNM_SetProjectMarker(proj, num, isrgn, pos, rgnend, name, color)
end


---Lua: boolean reaper.SNM_TagMediaFile(string fn, string tag, string tagval)
---
---
---[S&M] Tags a media file thanks to TagLib
---. Supported tags: "artist", "album", "genre", "comment", "title", or "year". Use an empty tagval to clear a tag. When a file is opened in REAPER, turn it offline before using this function. Returns false if nothing updated. See SNM_ReadMediaFileTag
---.
function reaper.SNM_TagMediaFile(fn, tag, tagval)
end


---Lua: reaper.SNM_TieResourceSlotActions(integer bookmarkId)
---
---
---[S&M] Attach Resources slot actions to a given bookmark.
function reaper.SNM_TieResourceSlotActions(bookmarkId)
end


---Lua: string reaper.ULT_GetMediaItemNote(MediaItem item)
---
---
---[ULT] Get item notes.
function reaper.ULT_GetMediaItemNote(item)
end


---Lua: reaper.ULT_SetMediaItemNote(MediaItem item, string note)
---
---
---[ULT] Set item notes.
function reaper.ULT_SetMediaItemNote(item, note)
end


---Lua: reaper.atexit(function)
---
---Adds code to be executed when the script finishes or is ended by the user. Typically used to clean up after the user terminates defer() or runloop() code.
function reaper.atexit(Function)
end


---Lua: reaper.defer(function)
---
---Adds code to be called back by REAPER. Used to create persistent ReaScripts that continue to run and respond to input, while the user does other tasks. Identical to runloop().
---Note that no undo point will be automatically created when the script finishes, unless you create it explicitly.
function reaper.defer(Function)
end


---Lua: reaper.get_action_context()
---
---is_new_value,filename,sectionID,cmdID,mode,resolution,val = reaper.get_action_context()
---Returns contextual information about the script, typically MIDI/OSC input values.
---val will be set to a relative or absolute value depending on mode (=0: absolute mode, >0: relative modes). resolution=127 for 7-bit resolution, =16383 for 14-bit resolution.
---Notes: sectionID, and cmdID will be set to -1 if the script is not part of the action list. mode, resolution and val will be set to -1 if the script was not triggered via MIDI/OSC.
function reaper.get_action_context()
end


---Lua: reaper.new_array([table|array][size])
---
---Creates a new reaper.array object of maximum and initial size size, if specified, or from the size/values of a table/array. Both size and table/array can be specified, the size parameter will override the table/array size.
function reaper.new_array(table_or_array_or_size)
    new_array = {}
    
    
    ---Lua: {reaper.array}.clear([value, offset, size])
    ---
    ---Sets the value of zero or more items in the array. If value not specified, 0.0 is used. offset is 1-based, if size omitted then the maximum amount available will be set.
    function new_array.clear(value, offset, size)
    end
    
    ---Lua: {reaper.array}.convolve([src, srcoffs, size, destoffs])
    ---
    ---Convolves complex value pairs from reaper.array, starting at 1-based srcoffs, reading/writing to 1-based destoffs. size is in normal items (so it must be even)
    function new_array.convolve(src, srcoffs, size, destoffs)
    end
    
    ---Lua: {reaper.array}.copy([src, srcoffs, size, destoffs])
    ---
    ---Copies values from reaper.array or table, starting at 1-based srcoffs, writing to 1-based destoffs.
    function new_array.copy(src, srcoffs, size, destoffs)
    end
    
    ---Lua: {reaper.array}.fft(size[, permute, offset])
    ---
    ---Performs a forward FFT of size. size must be a power of two between 4 and 32768 inclusive. If permute is specified and true, the values will be shuffled following the FFT to be in normal order.
    function new_array.fft(size, permute, offset)
    end
    
    ---Lua: {reaper.array}.fft_real(size[, permute, offset])
    ---
    ---Performs a forward real->complex FFT of size. size must be a power of two between 4 and 32768 inclusive. If permute is specified and true, the values will be shuffled following the FFT to be in normal order.
    function new_array.fft_real(size, permute, offset)
    end
    
    ---Lua: {reaper.array}.get_alloc()
    ---
    ---Returns the maximum (allocated) size of the array.
    function new_array.get_alloc()
    end
    
    ---Lua: {reaper.array}.ifft(size[, permute, offset])
    ---
    ---Performs a backwards FFT of size. size must be a power of two between 4 and 32768 inclusive. If permute is specified and true, the values will be shuffled before the IFFT to be in fft-order.
    function new_array.ifft(size, permute, offset)
    end
    
    ---Lua: {reaper.array}.ifft_real(size[, permute, offset])
    ---
    ---Performs a backwards complex->real FFT of size. size must be a power of two between 4 and 32768 inclusive. If permute is specified and true, the values will be shuffled before the IFFT to be in fft-order.
    function new_array.ifft_real(size, permute, offset)
    end
    
    ---Lua: {reaper.array}.multiply([src, srcoffs, size, destoffs])
    ---
    ---Multiplies values from reaper.array, starting at 1-based srcoffs, reading/writing to 1-based destoffs.
    function new_array.multiply(src, srcoffs, size, destoffs)
    end
    
    ---Lua: {reaper.array}.resize(size)
    ---
    ---Resizes an array object to size. size must be [0..max_size].
    function new_array.resize(size)
    end
    
    ---Lua: {reaper.array}.table([offset, size])
    ---
    ---Returns a new table with values from items in the array. Offset is 1-based and if size is omitted all available values are used.
    function new_array.table(offset, size)
    end
    
    return new_array
end


---Lua: reaper.runloop(function)
---
---Adds code to be called back by REAPER. Used to create persistent ReaScripts that continue to run and respond to input, while the user does other tasks. Identical to defer().
---Note that no undo point will be automatically created when the script finishes, unless you create it explicitly.
function reaper.runloop(Function)
end



reaper = {}
setmetatable(reaper, {
    __index = function(table, key)
        return original_reaper[key]
    end,

    __newindex = function(table, key, value)
        original_reaper[key] = value
    end
})


return reaper
