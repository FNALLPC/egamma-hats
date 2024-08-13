import ipywidgets as widgets
from IPython.display import clear_output
from ipywidgets import interactive


def calculate_efficiency(
    df, feature1_cut, feature2_cut, feature3_cut, feature4_cut, feature5_cut
):
    signal = df[
        (df["ele_hadronicOverEm"] >= feature1_cut)
        & (df["ele_ep"] >= feature2_cut)
        & (df["ele_pt"] >= feature3_cut)
        & (df["ele_ecalPFClusterIso"] >= feature4_cut)
        & (df["ele_hcalPFClusterIso"] >= feature5_cut)
        & (df["Type"] == "GoodElectrons")
    ]

    background = df[
        (df["ele_hadronicOverEm"] >= feature1_cut)
        & (df["ele_ep"] >= feature2_cut)
        & (df["ele_pt"] >= feature3_cut)
        & (df["ele_ecalPFClusterIso"] >= feature4_cut)
        & (df["ele_hcalPFClusterIso"] >= feature5_cut)
        & (df["Type"] == "JunkElectrons")
    ]

    signal_efficiency = len(signal) / len(df[df["Type"] == "GoodElectrons"])
    background_efficiency = len(background) / len(df[df["Type"] == "JunkElectrons"])

    return signal_efficiency, background_efficiency


def update_efficiency(
    feature1_cut, feature2_cut, feature3_cut, feature4_cut, feature5_cut
):
    signal_efficiency, background_efficiency = calculate_efficiency(
        df, feature1_cut, feature2_cut, feature3_cut, feature4_cut, feature5_cut
    )

    # Clear previous output
    with output:
        clear_output()

        # Print the new efficiency values
        print(f"Signal Efficiency: {signal_efficiency:.2f}")
        print(f"Background Efficiency: {background_efficiency:.2f}")


# Create sliders for the feature columns
percentile = 0.95
ele_hadronicOverEm_slider = widgets.FloatSlider(
    value=0,
    min=df["ele_hadronicOverEm"].min(),
    max=df["ele_hadronicOverEm"].quantile(percentile),
    step=0.1,
    description="ele_hadronicOverEm:",
)
ele_fbrem_slider = widgets.FloatSlider(
    value=0,
    min=df["ele_ep"].min(),
    max=df["ele_ep"].quantile(percentile),
    step=0.2,
    description="ele_ele_ep:",
)
ele_pt_slider = widgets.FloatSlider(
    value=0,
    min=df["ele_pt"].min(),
    max=df["ele_pt"].quantile(percentile),
    step=5,
    description="ele_pt:",
)
ele_hadronicOverEm_slider.layout.width = "800px"
ele_fbrem_slider.layout.width = "800px"
ele_hadronicOverEm_slider.layout.width = "800px"

ele_ecalPFClusterIso_slider = widgets.FloatSlider(
    value=0,
    min=df["ele_ecalPFClusterIso"].min(),
    max=df["ele_ecalPFClusterIso"].quantile(percentile),
    step=0.1,
    description="ele_ecalPFClusterIso:",
)
ele_hcalPFClusterIso_slider = widgets.FloatSlider(
    value=0,
    min=df["ele_hcalPFClusterIso"].min(),
    max=df["ele_hcalPFClusterIso"].quantile(percentile),
    step=0.1,
    description="ele_hcalPFClusterIso:",
)
ele_ecalPFClusterIso_slider.layout.width = "800px"
ele_hcalPFClusterIso_slider.layout.width = "800px"

# Create an output area to display the efficiency values
output = widgets.Output()

# Create an interactive function with the sliders and output
interactive_efficiency = interactive(
    update_efficiency,
    feature1_cut=ele_hadronicOverEm_slider,
    feature2_cut=ele_fbrem_slider,
    feature3_cut=ele_pt_slider,
    feature4_cut=ele_ecalPFClusterIso_slider,
    feature5_cut=ele_hcalPFClusterIso_slider,
)

# Display the sliders and the output area
display(interactive_efficiency)
display(output)
