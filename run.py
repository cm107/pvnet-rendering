from config import cfg
import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', action='store', dest='type', type=str)
args = parser.parse_args()


def run_rendering():
    from blender.render_utils import Renderer, YCBRenderer
    # YCBRenderer.multi_thread_render()
    # renderer = YCBRenderer('037_scissors')
    linemod_cls_names = [
        'ape', 'cam', 'cat',
        'duck', 'glue', 'iron',
        'phone', 'benchvise', 'can',
        'driller', 'eggbox', 'holepuncher',
        'lamp'
    ]
    for target in linemod_cls_names:
        renderer=Renderer(target)
        renderer.run()


def run_fuse():
    from fuse.fuse import run
    run()


if __name__ == '__main__':
    globals()['run_' + args.type]()
