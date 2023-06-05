from IPython.display import clear_output

def calculate_efficiency(df, feature1_cut, feature2_cut, feature3_cut, feature4_cut, feature5_cut):
    signal = df[(df['ele_hadronicOverEm'] >= feature1_cut) &
                (df["ele_ep"] >= feature2_cut) &
                (df['ele_pt'] >= feature3_cut) &
                (df['ele_ecalPFClusterIso'] >= feature4_cut) &
                (df['ele_hcalPFClusterIso'] >= feature5_cut) &
                (df['Type'] == 'GoodElectrons')]

    background = df[(df['ele_hadronicOverEm'] >= feature1_cut) &
                    (df["ele_ep"] >= feature2_cut) &
                    (df['ele_pt'] >= feature3_cut) &
                    (df['ele_ecalPFClusterIso'] >= feature4_cut) &
                    (df['ele_hcalPFClusterIso'] >= feature5_cut) &
                    (df['Type'] == 'JunkElectrons')]

    signal_efficiency = len(signal) / len(df[df['Type'] == 'GoodElectrons'])
    background_efficiency = len(background) / len(df[df['Type'] == 'JunkElectrons'])

    return signal_efficiency, background_efficiency

