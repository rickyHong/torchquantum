import subprocess
from torchpack.utils.logging import logger
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str)
    parser.add_argument('--name', type=str)

    parser.add_argument('--device', type=str)
    parser.add_argument('--hub', type=str, default=None)
    parser.add_argument('--valid', action='store_true')

    args = parser.parse_args()

    valid = '_valid' if args.valid else ''

    pres = ['python',
            'examples/eval.py',
            f'examples/configs/'
            f'{args.dataset}/{args.name}/eval/'
            f'{args.device}/real/opt2/noancilla/300_s18400{valid}.yml',
            '--jobs=5',
            '--verbose',
            f'--hub={args.hub}',
            '--run-dir']

    with open(f'logs/{args.device}/{args.dataset}.'
              f'{args.name}.nonoise_bnorm{valid}.u3cu3_0'
              f'.txt',
              'a') as \
            wfid:
        for node in [
                     'n2b1',
                     'n2b2',
                     'n2b3',
                     'n2b4',
                     'n3b1',
                     'n3b2',
                     'n4b1',
                     'n4b2'
                     ]:
            exp = f'runs/{args.dataset}.{args.name}.train.noaddnoise.' \
                  f'bnorm.u3cu3_0.{node}.default'
            logger.info(f"running command {pres + [exp]}")
            subprocess.call(pres + [exp], stderr=wfid)
