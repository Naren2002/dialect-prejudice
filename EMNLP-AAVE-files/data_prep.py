
def clean_text(txt):
    return txt.rstrip('\n').lstrip()

with open('./aave_samples.txt', 'r') as aae:
    with open('./sae_samples.txt', 'r') as sae:

        aae_lines = aae.readlines()
        sae_lines = sae.readlines()

        with open('../data/pairs/twitter_dataset.txt', 'w') as res:
            
            assert len(aae_lines) == len(sae_lines)
            for i in range(len(aae_lines)):
                res.write(clean_text(aae_lines[i]) + "\t" + clean_text(sae_lines[i]) + '\n')