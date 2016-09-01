import os


class RequiredOptError(Exception):
    """RequiredOptError"""


class oslo_concurrency(object):
    # Enables or disables inter-process locks.
    disable_process_locking = False

    # Directory to use for lock files.  For security, the
    # specified directory should only be writable by the user
    # running the processes that need locking.
    # Defaults to environment variable OSLO_LOCK_PATH.
    # If external locks are used, a lock path must be set.

    lock_path = os.environ.get("OSLO_LOCK_PATH")
