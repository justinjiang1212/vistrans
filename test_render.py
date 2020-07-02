import empress
from empress import recon_vis
from empress.miscs import input_generator

from sample_data import host_dict3, parasite_dict3, recon_dict3
from recon_viewer import render


recon_input = input_generator.generate_random_recon_input(1)
recongraph = empress.reconcile(recon_input, 2, 3, 1)
reconciliation = recongraph.median()

#render(recon_input.host_dict, recon_input.parasite_dict, reconciliation._reconciliation)
render(recon_input.host_dict, recon_input.parasite_dict, reconciliation._reconciliation, show_internal_labels=True, show_freq=False)


print(reconciliation._reconciliation)
