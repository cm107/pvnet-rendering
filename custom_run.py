from config import cfg
import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', action='store', dest='type', type=str)
parser.add_argument('--class_type', type=str)
parser.add_argument('--data_dir', type=str, default='custom_data')
parser.add_argument('--renders_dir', type=str, default='custom_renders')
parser.add_argument('--obj_path', type=str, default=None)
args = parser.parse_args()


def run_rendering(args):
    from blender.render_utils import Renderer, YCBRenderer
    # YCBRenderer.multi_thread_render()
    # renderer = YCBRenderer('037_scissors')
    renderer=Renderer(
        class_type=args.class_type,
        data_dir=args.data_dir,
        renders_dir=args.renders_dir,
        obj_path=args.obj_path
    )
    renderer.run()

def run_fuse():
    from fuse.fuse import run
    run()


if __name__ == '__main__':
    globals()['run_' + args.type](args)
