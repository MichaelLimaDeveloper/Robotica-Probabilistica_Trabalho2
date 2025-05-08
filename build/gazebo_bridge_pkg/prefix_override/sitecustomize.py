import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kifelix/ambiente_ws/install/gazebo_bridge_pkg'
