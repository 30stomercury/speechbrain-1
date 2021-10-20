# How to run
# Fine-tune based on a pretrained model (wav2vec, wav2vec_small or seq2seq)
`python3 train_with_wav2vec2.py hparams/train_with_wav2vec2_ngram.yaml --data_folder path/to/Syllables_rep --val_set chunki`

# Compute average wer across 4 chunks
`python3 compute_ave_wer.py --output_folder /your/save/folder # e.g., --output_folder ~/workspace/results/pretrained_wav2vec_syllables_1.2/`
