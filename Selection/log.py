python/DataPreselSequences_cff.py:    #process.basePreSel = cms.Sequence(process.hltPhysicsDeclared*process.noScraping*process.primaryVertexFilter)
python/DataPreselSequences_cff.py:    process.basePreSel = cms.Sequence(process.primaryVertexFilter) # 76x
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence( process.basePreSel*process.hltLevel1GTSeed )
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence( process.basePreSel*process.HBHENoiseFilter )
python/DataPreselSequences_cff.py:        process.inclusive_eg = cms.Sequence( process.eg_selector )        
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence( process.inclusive_eg*process.basePreSel )
python/DataPreselSequences_cff.py:        process.exclusive_eg = cms.Sequence( ~process.mu_selector*process.eg_selector )        
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence( process.exclusive_eg*process.basePreSel )
python/DataPreselSequences_cff.py:        process.inclusive_mu = cms.Sequence( process.mu_selector )
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence( process.inclusive_mu*process.basePreSel )
python/DataPreselSequences_cff.py:        process.exclusive_mu = cms.Sequence( ~process.eg_selector*process.mu_selector )
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence( process.exclusive_mu*process.basePreSel )
python/DataPreselSequences_cff.py:        process.inclusive_egmu = cms.Sequence( process.egmu_selector )
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence( process.inclusive_egmu*process.basePreSel )
python/DataPreselSequences_cff.py:        process.inclusive_jet = cms.Sequence( process.jet_selector )
python/DataPreselSequences_cff.py:        process.basePreSel = cms.Sequence(process.inclusive_jet*process.basePreSel )    
python/ElectronExtra_cff.py:    process.mvaID = cms.Sequence(  process.mvaTrigV0 + process.mvaTrigNoIPV0 + process.mvaNonTrigV0 )
python/ElectronExtra_cff.py:    process.pfIsolationSequence = cms.Sequence(
python/ElectronExtra_cff.py:    process.EleEmbedSequence = cms.Sequence(process.selectedPrimaryVertices * process.selectedPatElectronsUserEmbedded)
python/JetMETExtra_cff.py:    #process.FastJetSequence = cms.Sequence(process.kt6PFJets * process.ak5PFJets)
python/JetMETExtra_cff.py:    process.RecoMetSequence = cms.Sequence(process.pfCandMETcorr * process.pfchsMETcorr *
python/JetMETExtra_cff.py:    #    process.ResJetCorSequence = cms.Sequence(process.selectedPatJetsResCor*process.puJetIdResCor*process.puJetMvaResCor)
python/LocalRunSkeleton_cff.py:#process.makePatElectrons = cms.Sequence( process.eIdSequence * process.simpleEleIdSequence * process.electronMatch * process.patElectrons )
python/MuonExtra_cff.py:    process.produceMuonPFIsoPrePat = cms.Sequence(
python/MuonExtra_cff.py:    process.diMuVetoFilter = cms.Sequence(process.globalMuons*process.diMuonVeto)
python/pfToPatSequences_cff.py:    process.eidCiCSequence = cms.Sequence(
python/pfToPatSequences_cff.py:    process.patSequence = cms.Sequence(
python/ttSemiLepKinFitElectron_cff.py:    process.kinFitSequence = cms.Sequence(process.cleanPatElectronsUser* process.cleanPatJetsUser* process.cleanPatJetsResCor* process.kinFitTtSemiLepEvent)
python/ttSemiLepKinFitMuon_cff.py:    #process.kinFitSequence = cms.Sequence(process.cleanPatJetsResCor* process.kinFitTtSemiLepEvent)
python/ttSemiLepKinFitMuon_cff.py:    process.kinFitSequence = cms.Sequence(process.kinFitTtSemiLepEvent)
test/ttSemiLepKinFitMuon_cfg.py:#process.kinFitSequence = cms.Sequence(process.kinFitTtSemiLepEvent)
test/ttSemiLepKinFitMuon_cfg.py:#process.kinFitSequence = cms.Sequence(process.cleanPatJetsResCor* process.kinFitTtSemiLepEvent)