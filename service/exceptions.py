"""
Atmosphere service exceptions.
"""


class ActionNotAllowed(Exception):
    def __init__(self, message):
        self.message = message
        self.status_code = 409
        super(ActionNotAllowed, self).__init__()

class UnderThresholdError(Exception):
    def __init__(self, message):
        self.message = message
        self.status_code = 400
        super(UnderThresholdError, self).__init__()

class SecurityGroupNotCreated(Exception):

    def __init__(self):
        self.message = "Gateway Timeout! Security Group(s) could not be created. Please try again later"
        self.status_code = 504
        super(SecurityGroupNotCreated, self).__init__()

    def __str__(self):
        return "%s" % (self.message, )
class HypervisorCapacityError(Exception):

    def __init__(self, hypervisor, message):
        self.hypervisor = hypervisor
        self.message = message
        super(HypervisorCapacityError, self).__init__(self.message)


class OverAllocationError(Exception):

    def __init__(self, wait_timedelta):
        self.wait_timedelta = wait_timedelta
        self.message = "Time allocation exceeded. "\
            "Wait %s before requesting new resources"\
            % (self.wait_timedelta)
        super(OverAllocationError, self).__init__(self.message)

    def __str__(self):
        return "%s" % (self.message, )


class OverQuotaError(Exception):

    def __init__(self, resource=None, requested=None,
                 used=None, limit=None, message=None):
        if not message:
            self.message = "Quota exceeded: Requested %s %s but already used "\
                           "%s/%s %s."\
                           % (requested, resource, used, limit, resource)
        else:
            self.message = message
        super(OverQuotaError, self).__init__(self.message)

    def __str__(self):
        return "%s" % (self.message, )


class DeviceBusyException(Exception):

    def __init__(self, mount_loc, process_list):
        proc_str = ''
        for proc_name, pid in process_list:
            proc_str += '\nProcess name:%s process id:%s' % (proc_name, pid)
        message = "Volume mount location is: %s\nRunning processes that"\
                  " are accessing that directory must be closed before "\
                  "unmounting. All offending processes names and IDs are "\
                  "listed below:%s" % (mount_loc, proc_str)
        self.message = message
        #Exception.__init__(self, message)
        super(DeviceBusyException, self).__init__(mount_loc, process_list)

    def __str__(self):
        return "%s:\n%s" % (self.message, repr(self.process_list))


class SizeNotAvailable(Exception):

    def __init__(self):
        self.message = "Size Not Available."
        super(SizeNotAvailable, self).__init__()

    def __str__(self):
        return "%s" % (self.message, )

class VolumeAttachConflict(Exception):

    def __init__(self, instance_id, volume_id):
        self.message = "Volume %s is still attached to instance %s"\
                % (volume_id, instance_id)
        super(VolumeAttachConflict, self).__init__()

    def __str__(self):
        return "%s" % (self.message, )

class VolumeMountConflict(Exception):

    def __init__(self, instance_id, volume_id, extra=None):
        self.message = "Volume %s could not be auto-mounted to %s. %s"\
                " See Available Volumes -> Mounting a Volume "\
                " to learn how to mount the device manually"\
                % (volume_id, instance_id, "Reason:%s" % extra)
        super(VolumeMountConflict, self).__init__()

    def __str__(self):
        return "%s" % (self.message, )
