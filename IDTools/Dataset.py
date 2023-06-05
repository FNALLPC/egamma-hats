processes=[
    {'Class':'GoodPhotons','path':('/mnt/hdfs/store/group/phys_egamma/HATS2021/ID_Training/GJet/','.root'),
     'xsecwt': 1,
     'selection':'(phoPt > 10) & (abs(phoEta) < 2.5) & (isPhotonMatching==1)'
    },
    {'Class':'Junk','path':('/mnt/hdfs/store/group/phys_egamma/HATS2021/ID_Training/GJet/','.root'),
     'xsecwt': 1,
     'selection':'(phoPt > 10) & (abs(phoEta) < 2.5)  & (isPhotonMatching==0)',
    }
]

branches=['phoHoverE', # in NanoAOD as Photon_hoe
          'photrkSumPtHollow', # in MiniAOD as photon.trkSumPtHollowConeDR03
          'photrkSumPtSolid', # in MiniAOD as photon.trkSumPtSolidConeDR03
          'phosigmaIetaIeta', #in NanoAOD as Photon_sieie
          'phoSigmaIEtaIEtaFull5x5', #in MiniAOD as photon.SigmaIEtaIEtaFull5x5
          'phoSigmaIEtaIPhiFull5x5', # in MiniAOD as photon.SigmaIEtaIPhiFull5x5
          'phoEcalPFClusterIso', # in MiniAOD as photon.EcalPFClusterIso
          'phoHcalPFClusterIso', # in MiniAOD as photon.HcalPFClusterIso
          'phohasPixelSeed', # in NanoAOD as Photon_pixelSeed
          'phoR9Full5x5',# in NanoAOD as Photon_r9
          "phoPt", # in NanoAOD as Photon_pt
          'phoEta', # in NanoAOD as Photon_eta
          "isPhotonMatching", # A custom variable (can be built in nanoAOD from Photon_genPartFlav)
          "isPFPhoton" # A custom variable (not available in nanoAOD)
         ]

ele_branches=["scl_eta",
          "ele_pt",
          "matchedToGenEle",
          "matchedToGenPhoton",
          "matchedToGenTauJet",
          "matchedToHadron",
          "ele_convDist",
          "ele_convDcot",
          "EleMVACats",
          "ele_fbrem","ele_deltaetain", "ele_deltaphiin", "ele_oldsigmaietaieta", 
          "ele_oldhe", "ele_ep", "ele_olde15", "ele_eelepout",
          "ele_kfchi2", "ele_kfhits", "ele_expected_inner_hits","ele_dr03TkSumPt",
          "ele_dr03EcalRecHitSumEt","ele_dr03HcalTowerSumEt",
          "ele_ecalPFClusterIso","ele_hcalPFClusterIso",
          "ele_gsfchi2",
          'ele_conversionVertexFitProbability',
          "ele_nbrem",'ele_deltaetaseed','ele_hadronicOverEm','ele_olde25max','ele_olde55','passElectronSelection']