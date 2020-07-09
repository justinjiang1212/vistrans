import empress
from empress import recon_vis
from empress.miscs import input_generator

from recon_viewer import render


recon_input = input_generator.generate_random_recon_input(15)
recongraph = recon_input.reconcile(1, 1, .0001)
reconciliation = recongraph.median()


host_dict = {'hTop': ('Top', 'h0', ('h0', 'h1'), ('h0', 'h4')), ('h0', 'h1'): ('h0', 'h1', ('h1', 'h2'), ('h1', 'h3')), ('h1', 'h2'): ('h1', 'h2', None, None), ('h1', 'h3'): ('h1', 'h3', None, None), ('h0', 'h4'): ('h0', 'h4', ('h4', 'h5'), ('h4', 'h10')), ('h4', 'h5'): ('h4', 'h5', 
('h5', 'h6'), ('h5', 'h7')), ('h5', 'h6'): ('h5', 'h6', None, None), ('h5', 'h7'): ('h5', 'h7', ('h7', 'h8'), ('h7', 'h9')), ('h7', 'h8'): ('h7', 'h8', None, None), ('h7', 'h9'): ('h7', 'h9', None, None), ('h4', 'h10'): ('h4', 'h10', ('h10', 'h11'), ('h10', 'h18')), ('h10', 'h11'): ('h10', 'h11', ('h11', 'h12'), ('h11', 'h15')), ('h11', 'h12'): ('h11', 'h12', ('h12', 'h13'), ('h12', 'h14')), ('h12', 'h13'): ('h12', 'h13', None, None), ('h12', 'h14'): ('h12', 'h14', None, None), ('h11', 'h15'): ('h11', 'h15', ('h15', 'h16'), ('h15', 'h17')), ('h15', 'h16'): ('h15', 'h16', None, None), ('h15', 'h17'): ('h15', 'h17', None, None), ('h10', 'h18'): ('h10', 'h18', ('h18', 'h19'), ('h18', 'h20')), ('h18', 'h19'): ('h18', 'h19', None, None), ('h18', 'h20'): ('h18', 'h20', ('h20', 'h21'), ('h20', 'h24')), ('h20', 'h21'): ('h20', 'h21', ('h21', 'h22'), ('h21', 'h23')), ('h21', 'h22'): ('h21', 'h22', None, None), ('h21', 'h23'): ('h21', 'h23', None, None), ('h20', 'h24'): ('h20', 'h24', ('h24', 'h25'), ('h24', 'h26')), ('h24', 'h25'): ('h24', 'h25', None, None), ('h24', 'h26'): ('h24', 'h26', ('h26', 'h27'), ('h26', 'h28')), ('h26', 'h27'): ('h26', 'h27', None, None), ('h26', 'h28'): ('h26', 'h28', None, None)}

parasite_dict = {'pTop': ('Top', 'p0', ('p0', 'p1'), ('p0', 'p10')), ('p0', 'p1'): ('p0', 'p1', ('p1', 'p2'), ('p1', 'p3')), ('p1', 'p2'): ('p1', 'p2', None, None), ('p1', 'p3'): ('p1', 'p3', ('p3', 'p4'), ('p3', 'p7')), ('p3', 'p4'): ('p3', 'p4', ('p4', 'p5'), ('p4', 'p6')), ('p4', 'p5'): ('p4', 'p5', None, None), ('p4', 'p6'): ('p4', 'p6', None, None), ('p3', 'p7'): ('p3', 'p7', ('p7', 'p8'), ('p7', 'p9')), ('p7', 'p8'): ('p7', 'p8', None, None), ('p7', 'p9'): ('p7', 'p9', None, None), ('p0', 'p10'): ('p0', 'p10', ('p10', 'p11'), ('p10', 'p20')), ('p10', 'p11'): ('p10', 'p11', ('p11', 'p12'), ('p11', 'p13')), ('p11', 'p12'): ('p11', 'p12', None, None), ('p11', 'p13'): ('p11', 'p13', ('p13', 'p14'), ('p13', 'p17')), ('p13', 'p14'): ('p13', 'p14', ('p14', 'p15'), ('p14', 'p16')), ('p14', 'p15'): ('p14', 'p15', None, None), ('p14', 'p16'): ('p14', 'p16', None, None), ('p13', 'p17'): ('p13', 'p17', ('p17', 'p18'), ('p17', 'p19')), ('p17', 'p18'): ('p17', 'p18', None, None), ('p17', 'p19'): ('p17', 'p19', None, None), ('p10', 'p20'): ('p10', 'p20', ('p20', 'p21'), ('p20', 'p22')), ('p20', 'p21'): ('p20', 'p21', None, None), ('p20', 'p22'): ('p20', 'p22', ('p22', 'p23'), ('p22', 'p24')), ('p22', 'p23'): ('p22', 'p23', None, None), ('p22', 'p24'): ('p22', 'p24', ('p24', 'p25'), ('p24', 'p26')), ('p24', 'p25'): ('p24', 'p25', None, None), ('p24', 'p26'): ('p24', 'p26', ('p26', 'p27'), ('p26', 'p28')), ('p26', 'p27'): ('p26', 'p27', None, None), ('p26', 'p28'): ('p26', 'p28', None, None)}

recon = {('p0', 'h0'): [('S', ('p1', 'h1'), ('p10', 'h4'))], ('p1', 'h1'): [('T', ('p3', 'h1'), ('p2', 'h14'))], ('p3', 'h1'): [('T', ('p4', 'h1'), ('p7', 'h4'))], ('p4', 'h1'): [('L', ('p4', 'h2'), (None, None))], ('p4', 'h2'): [('T', ('p6', 'h2'), ('p5', 'h23'))], ('p6', 'h2'): [('C', (None, None), (None, None))], ('p5', 'h23'): [('C', (None, None), (None, None))], ('p7', 'h4'): [('S', ('p9', 'h5'), ('p8', 'h10'))], ('p9', 'h5'): [('L', ('p9', 'h7'), (None, None))], ('p9', 'h7'): [('L', ('p9', 'h8'), (None, None))], ('p9', 'h8'): [('C', (None, 
None), (None, None))], ('p8', 'h10'): [('L', ('p8', 'h11'), (None, None))], ('p8', 'h11'): [('L', ('p8', 'h15'), (None, None))], ('p8', 'h15'): [('L', ('p8', 'h17'), (None, None))], ('p8', 'h17'): [('C', (None, None), (None, None))], ('p2', 'h14'): [('C', (None, None), (None, None))], ('p10', 'h4'): [('S', ('p20', 'h5'), ('p11', 'h10'))], ('p20', 'h5'): [('T', ('p22', 'h5'), ('p21', 'h13'))], ('p22', 'h5'): [('L', ('p22', 'h7'), (None, None))], ('p22', 'h7'): [('L', ('p22', 'h8'), (None, None))], ('p22', 'h8'): [('T', ('p23', 'h8'), ('p24', 'h20'))], ('p23', 'h8'): [('C', (None, None), (None, None))], ('p24', 'h20'): [('S', ('p25', 'h21'), ('p26', 'h24'))], ('p25', 'h21'): [('L', ('p25', 'h22'), (None, None))], ('p25', 'h22'): [('C', (None, None), (None, None))], ('p26', 'h24'): [('T', ('p28', 'h24'), ('p27', 'h8'))], ('p28', 'h24'): [('L', ('p28', 'h25'), (None, None))], ('p28', 'h25'): [('C', (None, None), (None, None))], ('p27', 'h8'): [('C', (None, None), (None, None))], ('p21', 'h13'): [('C', (None, None), (None, None))], ('p11', 'h10'): [('S', ('p13', 'h11'), ('p12', 'h18'))], ('p13', 'h11'): [('L', ('p13', 'h15'), (None, None))], ('p13', 'h15'): [('S', ('p14', 'h16'), ('p17', 'h17'))], ('p14', 'h16'): [('D', ('p15', 'h16'), ('p16', 'h16'))], ('p15', 'h16'): [('C', (None, None), (None, None))], ('p16', 'h16'): [('C', (None, None), (None, None))], ('p17', 'h17'): [('T', ('p18', 'h17'), ('p19', 'h8'))], ('p18', 'h17'): [('C', (None, None), (None, None))], ('p19', 'h8'): [('C', (None, None), (None, None))], ('p12', 'h18'): [('L', ('p12', 'h20'), (None, None))], ('p12', 'h20'): [('L', ('p12', 'h24'), (None, None))], ('p12', 'h24'): [('L', ('p12', 'h25'), (None, None))], ('p12', 'h25'): [('C', (None, None), (None, None))]}


render(recon_input.host_dict, recon_input.parasite_dict, reconciliation._reconciliation, show_internal_labels=True, show_freq=False)
#render(host_dict, parasite_dict, recon, show_internal_labels=True, show_freq=False)


