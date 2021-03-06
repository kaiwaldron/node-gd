import Options
from os import unlink, symlink, popen
from os.path import exists
import sys

srcdir = "."
blddir = "build"
VERSION = "0.0.1"

def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  if sys.platform == 'darwin':
    conf.env.CPPPATH = ['/opt/local/include']
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")

def build(bld):
  bld.env.append_value('LINKFLAGS', ['-lgd', '-L/opt/local/lib'])
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.target = "node-gd"
  obj.source = "node-gd.cc"
  obj.lib    = "gd"
 
def shutdown():
  if Options.commands['clean']:
    if exists('node-gd.node'): unlink('node-gd.node')
