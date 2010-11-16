from shootblues.common import forceStartService, forceStopService, log
import blue
import service

class SessionTimerSvc(service.Service):
    __guid__ = "svc.sessiontimer"
    __update_on_reload__ = 0
    __exportedcalls__ = {}
    __notifyevents__ = [
        "OnSessionChanged"
    ]

    def __init__(self):
        service.Service.__init__(self)

    def OnSessionChanged(self, isRemote, session, change):
        log("Session changed, timer suppressed.")
        session.nextSessionChange = blue.os.GetTime(1) + 1

forceStartService("sessiontimer", SessionTimerSvc)

def __unload__():
    forceStopService("sessiontimer")