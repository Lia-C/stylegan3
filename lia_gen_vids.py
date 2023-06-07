import os
pkl_num = "000220"
network = f"training_results/00001-stylegan3-r-main_dataset_papercuts_clean_ish_converted_for_sg3-gpus4-batch8-gamma6.6/network-snapshot-{pkl_num}.pkl"


output_basedir = "training_results/00001-stylegan3-r-main_dataset_papercuts_clean_ish_converted_for_sg3-gpus4-batch8-gamma6.6"

psi = 1

seeds = "0-3"
num_keyframes = 4
w_frames = 30

outfname = f"lerp_seeds_{seeds}_num_keyframes_{num_keyframes}_w_frames_{w_frames}_psi_{psi}_with_pkl_{pkl_num}"

#    The animation length is either determined based on the --seeds value or explicitly
    # specified using the --num-keyframes option.

    # When num keyframes is specified with --num-keyframes, the output video length
    # will be 'num_keyframes*w_frames' frames.

cmd = f"python gen_video.py --network={network} --seeds={seeds} --num-keyframes={num_keyframes} --w-frames={w_frames} --trunc={psi} --output={output_basedir}/{outfname}.mp4"

os.system(cmd)

