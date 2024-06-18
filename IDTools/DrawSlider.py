def make_slider(prompt_electrons,unmatched_electrons):
    
    import pandas as pd
    import ipywidgets as widgets

    from ipywidgets import interact, interactive, fixed, interact_manual
    #from IDTools.calculate_efficiency import *

    from IPython.display import clear_output

    def cut(electrons):
        return electrons[(electrons.pt > 10) & (abs(electrons.eta) < 1.4447)]
    sig = cut(prompt_electrons)
    bkg = cut(unmatched_electrons)
    
    def calculate_efficiency(sig,bkg,feature1_cut, feature2_cut,feature3_cut):
        signal=sig[(sig.sieie<feature1_cut) & (sig.hoe<feature2_cut) & (sig.pfRelIso03_chg<feature3_cut)]
        background=bkg[(bkg.sieie<feature1_cut) & (bkg.hoe<feature2_cut) & (bkg.pfRelIso03_chg<feature3_cut)]

        signal_efficiency = len(signal) / len(sig)
        background_efficiency = len(background) / len(bkg)

        return signal_efficiency, background_efficiency

    def update_efficiency(feature1_cut, feature2_cut, feature3_cut):
        signal_efficiency, background_efficiency = calculate_efficiency(sig,bkg, feature1_cut, feature2_cut, feature3_cut)

        # Clear previous output
        with output:
            clear_output()

            # Print the new efficiency values
            print(f'Signal Efficiency: {signal_efficiency:.2f}')
            print(f'Background Efficiency: {background_efficiency:.2f}')
    
    # Create sliders for the feature columns
    percentile=0.95
    ele_hadronicOverEm_slider = widgets.FloatSlider(value=0.2, min=min(prompt_electrons.hoe), max=0.2, step=0.01,
                                                    description='hadronicOverEm:')
    ele_sieie_slider = widgets.FloatSlider(value=max(prompt_electrons.sieie), min=min(prompt_electrons.sieie), max=0.05, step=0.001, description='sieie:')
    ele_pfRelIso03_chg_slider = widgets.FloatSlider(value=1, min=min(prompt_electrons.pfRelIso03_chg), max=1, step=0.01, description='pfRelIso03:')
    #ele_pt_slider = widgets.FloatSlider(value=0, min=df['ele_pt'].min(), max=df['ele_pt'].quantile(percentile), step=5, description='ele_pt:')
    ele_hadronicOverEm_slider.layout.width = '800px'
    ele_sieie_slider.layout.width = '800px'
    ele_pfRelIso03_chg_slider.layout.width = '800px'

    # Create an output area to display the efficiency values
    output = widgets.Output()

    # Create an interactive function with the sliders and output
    interactive_efficiency = interactive(
        update_efficiency,
        feature1_cut=ele_hadronicOverEm_slider,
        feature2_cut=ele_sieie_slider,
        feature3_cut=ele_pfRelIso03_chg_slider,
    )

    # Display the sliders and the output area
    display(interactive_efficiency)
    display(output)