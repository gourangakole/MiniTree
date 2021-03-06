import FWCore.ParameterSet.Config as cms

scaledJetEnergy = cms.EDProducer("JetEnergyScale",
    inputJets            = cms.InputTag("slimmedJets"),
    inputMETs            = cms.InputTag("slimmedMETs"),
    scaleFactor          = cms.double(1.0),
    scaleFactorB         = cms.double(1.0),
    scaleType            = cms.string("abs"), #abs or rel(*eta) or jes:up / jes:down (pt-dependend)
    payload              = cms.string("AK4PF"), #jet and constituent type in JetMET convention
    jetPTThresholdForMET = cms.double(10.),
    jetEMLimitForMET     = cms.double(0.9),
    resolutionFactors    = cms.vdouble(1.0), # list the different JER factors here: (JER1, JER2)
    resolutionEtaRanges  = cms.vdouble(0, -1),  # list the |eta| ranges for the different JER factors here (etaMin1, etaMax1, etaMin2, etaMax2), etaMax=-1: means |eta|<infinity
    JECUncSrcFile        = cms.FileInPath("MiniTree/Utilities/data/80X_mcRun2_asymptotic_2016_TrancheIV_v6_Uncertainty_AK4PF.txt"),
    resolutionsFile   = cms.FileInPath("MiniTree/Utilities/data/Spring16_25nsV10_MC_PtResolution_AK4PF.txt"),
    scaleFactorsFile  = cms.FileInPath("MiniTree/Utilities/data/Spring16_25nsV10_MC_SF_AK4PF.txt")
)
