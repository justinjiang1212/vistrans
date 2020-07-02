import empress
from empress import recon_vis
from empress.miscs import input_generator

from recon_viewer import render


recon_input = input_generator.generate_random_recon_input(50)
recongraph = empress.reconcile(recon_input, 0, 0, 0)
reconciliation = recongraph.median()

#render(recon_input.host_dict, recon_input.parasite_dict, reconciliation._reconciliation)
render(recon_input.host_dict, recon_input.parasite_dict, reconciliation._reconciliation, show_internal_labels=True, show_freq=False)


