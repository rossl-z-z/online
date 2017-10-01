from pathlib import Path
import os

reload = True

#
# Server hooks
#
#   post_fork - Called just after a worker has been forked.
#
#       A callable that takes a server and worker instance
#       as arguments.
#
#   pre_fork - Called just prior to forking the worker subprocess.
#
#       A callable that accepts the same arguments as after_fork
#
#   pre_exec - Called just prior to forking off a secondary
#       master process during things like config reloading.
#
#       A callable that takes a server instance as the sole argument.
#

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

    ## os.system("export JAVA_HOME=~/jre1.8.0_152; export PATH=\"$JAVA_HOME/bin:$PATH\"; java -jar ditaa.jar ditaa_test.txt")

    jre_dir = Path("/opt/app-root/src/jre1.8.0_152")
    if jre_dir.is_dir():
        pass
    else:
        print("Installing Java JRE")
        os.system("wget http://download.java.net/java/jdk8u152/archive/b05/binaries/jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz")
        os.system("tar -xvf jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz")
        os.system("rm jre-8u152-ea-bin-b05-linux-x64-20_jun_2017.tar.gz")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    ## get traceback info
    import threading, sys, traceback
    id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""),
            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename,
                lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
