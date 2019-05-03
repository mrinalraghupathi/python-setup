from subprocess import check_call, Popen
from argparse import ArgumentParser

with open('labextensions.txt', 'r') as f:   
    jl_extensions = [line.strip() for line in f]


def activate_env(name):
    cmd = ['conda', 'activate', name]
    check_call(cmd)

def setup(env_name):
    activate_env(env_name)
    check_call(['conda', 'env', 'create', '-n', env_name, '-f', 'env.yaml'])


def setup_jl(name):
    activate_env(name)
    for jl in jl_extensions:
        check_call(['jupyter', 'labextension', 'install', '--no-build', jl])
    check_call(['jupyter', 'lab', 'build'])


 
p = ArgumentParser()
p.add_argument('-e', '--env_only', action="store_true", default=False)
p.add_argument('-j', '--jl_only', action="store_true", default=False)
p.add_argument('-a', '--all', action="store_true", default=False)
p.add_argument('env_name')
if __name__ == '__main__':

    args = p.parse_args()
    env_name = args.env_name
    if args.all:
        args.jl_only = True
        args.env_only = True
    if args.jl_only:
        setup_jl(env_name)
    if args.env_only:
        setup(env_name=env_name)
