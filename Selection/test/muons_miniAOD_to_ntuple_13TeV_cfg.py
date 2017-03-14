import FWCore.ParameterSet.Config as cms
from MiniTree.Selection.LocalRunSkeleton_cff import *
from MiniTree.Selection.ttSemiLepKinFitMuon_cff import *
from MiniTree.Selection.LocalSources_cff import toPrint

#INPUT FILE
#input_fileName = "/store/data/Run2016B/SingleMuon/MINIAOD/03Feb2017_ver1-v1/100000/08AD7B2D-34EE-E611-A7DA-001E674DA2E8.root"
input_fileName = "/store/mc/RunIISpring16MiniAODv1/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FED53EE4-7D16-E611-AE17-B083FED406AD.root"
#input_fileName = ["file:FEDED4C8-573B-E611-9ED6-0025904CF102.root"]
process.source.fileNames = [input_fileName]
process.maxEvents.input = cms.untracked.int32(500)

#OUTPUT FILE
import datetime
today_date = datetime.date.today()
sample_name = input_fileName.split("/")[4].split("_")[0]
output_fileName = sample_name+"_ntuple_"+str(today_date)+"_muons.root"
process.TFileService.fileName = cms.string(output_fileName)

#CONFIG PARAMETERS -----------------------------------------------------------
procName='LOCALUSER'
trigMenu = 'HLT'
#trigMenu = 'HLT2' #https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD
isData=False
isFastsim = False
#Trigger list
mutriglist = [ 'HLT_IsoMu27_v3' ]
egtriglist = [ 'HLT_Ele27_eta2p1_WPLoose_Gsf_v2']
jettriglist = [ 'HLT_JetE30_NoBPTX_v2' ]
trigpath = ''
#Extra modules
applyResJEC=False
addPF2PAT=False
storeOutPath=False
filterHBHEnoise = False
producePDFweights=False
isAOD = False
#START PROCESS CONFIGURATION -------------------------------------------------
process.setName_(procName)
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
#process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_miniAODv2_v1')
process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v6')

#CONFIGURE THE EXTRA MODULE -------------------------------------------------
if(addPF2PAT):
    toPrint("Adding PF2PAT objects","")
    addpf2PatSequence(process, not isData)
defineBasePreSelection(process,False, False)

#configureTauProduction(process, not isData)
###addJetMETExtra(process,isData,applyResJEC,isAOD)
addTriggerMatchExtra(process,egtriglist,mutriglist,jettriglist,False,trigMenu)
defineGenUtilitiesSequence(process)
#configureElectronMVAIdIso(process)
addSemiLepKinFitMuon(process, isData) #important

# ADD THE ANALYSIS MODULE ----------------------------------------------------
process.load('MiniTree.Selection.selection_cfi')
process.myMiniTreeProducer.MCTruth.isData = cms.bool(isData)
process.myMiniTreeProducer.MCTruth.sampleCode = cms.string(sample_name)
process.myMiniTreeProducer.MCTruth.producePDFweights = cms.bool(producePDFweights)
process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('muon')
process.myMiniTreeProducer.minEventQualityToStore = cms.int32(0)
process.myMiniTreeProducer.Trigger.source = cms.InputTag('TriggerResults::'+trigMenu)
process.myMiniTreeProducer.Trigger.bits = cms.vstring()
process.myMiniTreeProducer.Trigger.bits = mutriglist
process.myMiniTreeProducer.Trigger.bits.extend( egtriglist )
process.myMiniTreeProducer.Trigger.bits.extend( jettriglist )
process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(True)

#ANALYSIS SEQUENCE ------------------------------------------------------------
###process.met_extra = cms.Path(process.RecoMetSequence * process.patPfMetT0pcT1Txy)

###process.kineFit = cms.Path(process.kinFitSequence) #cms.Path(process.kinFitTtSemiLepEvent) #important


#process.ele_extra = cms.Path(process.mvaID + process.pfIsolationSequence)
#process.ele_embed = cms.Path(process.EleEmbedSequence)

###process.p  = cms.Path(process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
###process.schedule = cms.Schedule(process.kineFit, process.p)

process.p  = cms.Path(process.kinFitSequence*process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
process.schedule = cms.Schedule(process.p)

#if( addPF2PAT ):
#    process.pat_default = cms.Path( process.patSequence * process.patDefaultSequence * process.puJetIdSqeuence)
#else :
#    process.pat_default = cms.Path( process.patDefaultSequence * process.puJetIdSqeuence)

#process.schedule = cms.Schedule(process.ele_extra, process.pat_default, process.met_extra, process.ele_embed, process.kineFit, process.p)
#process.schedule = cms.Schedule(process.met_extra, process.kineFit, process.p)
#process.schedule = cms.Schedule(process.met_extra, process.p) #important

checkProcessSchedule(storeOutPath,True)

