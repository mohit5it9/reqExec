"""
Entrypoint to reqExec
"""

import sys
from config import Config
from executor import Executor

def main():
    """
    Calls the executor to execute a script along with required job
    config
    """
    if len(sys.argv) < 2:
        print 'Missing script name'
        sys.exit(1)
    elif len(sys.argv) < 3:
        print 'Missing job ENVs path'
        sys.exit(1)
    else:
        script_path = sys.argv[1]
        job_envs_path = sys.argv[2]

    config = Config(script_path, job_envs_path)
    ex = Executor(config)
    ex.execute()
    sys.exit(ex.exit_code)

if __name__ == '__main__':
    main()
