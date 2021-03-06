import FWCore.ParameterSet.Config as cms
from MiniTree.Selection.LocalRunSkeleton_cff import *
from MiniTree.Selection.ttSemiLepKinFitMuon_cff import *
from MiniTree.Selection.LocalSources_cff import toPrint

#INPUT FILE
isData=False
#inFile = "/store/data/Run2016B/SingleMuon/MINIAOD/23Sep2016-v3/00000/00AE0629-1F98-E611-921A-008CFA1112CC.root"
#inFile = "/store/data/Run2016H/SingleElectron/MINIAOD/03Feb2017_ver3-v1/110000/02973E99-69EC-E611-9913-5065F381A2F1.root"

#............ MC...........
#inFile = ["file:FEDED4C8-573B-E611-9ED6-0025904CF102.root"]
#POWHEG TT Jets
inFile = "/store/mc/RunIISummer16MiniAODv2/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0693E0E7-97BE-E611-B32F-0CC47A78A3D8.root"
process.source.fileNames = [inFile]
process.maxEvents.input = cms.untracked.int32(2000)

#OUTPUT FILE
import datetime
date = datetime.date.today()
samp_code = inFile.split("/")[4].split("_")[0]
outFile = samp_code+"_ntuple_"+str(date)+"_muons.root"
#process.TFileService.fileName = cms.string(outFile)
#for multi CRAB
process.TFileService.fileName = cms.string("outFile_.root")

#CONFIG PARAMETERS -----------------------------------------------------------
procName='LOCALUSER'
#trigMenu = 'HLT2' #https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD
trigMenu = 'HLT'
isFastsim = False
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
process.GlobalTag.globaltag  = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v6')

#CONFIGURE THE EXTRA MODULE -------------------------------------------------
if(addPF2PAT):
    toPrint("Adding PF2PAT objects","")
    addpf2PatSequence(process, not isData)
defineBasePreSelection(process,False, False)

#configureTauProduction(process, not isData)
#addJetMETExtra(process,isData,applyResJEC,isAOD)
#addTriggerMatchExtra(process,egtriglist,mutriglist,jettriglist,False,trigMenu)
defineGenUtilitiesSequence(process)
#configureElectronMVAIdIso(process)
addSemiLepKinFitMuon(process, isData) #important

# ADD THE ANALYSIS MODULE ----------------------------------------------------
process.load('MiniTree.Selection.selection_cfi')
process.myMiniTreeProducer.MCTruth.isData = cms.bool(isData)
if isData:
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("DATA")
else:
    #process.myMiniTreeProducer.MCTruth.sampleCode = cms.string(samp_code)
    #for multi CRAB
    process.myMiniTreeProducer.MCTruth.sampleCode = cms.string("sampCode_")
process.myMiniTreeProducer.MCTruth.producePDFweights = cms.bool(producePDFweights)
process.myMiniTreeProducer.minEventQualityToStore = cms.int32(1)
process.myMiniTreeProducer.Trigger.source = cms.InputTag('TriggerResults::'+trigMenu)
#process.myMiniTreeProducer.Trigger.bits = cms.vstring()
#process.myMiniTreeProducer.Trigger.bits = mutriglist
#process.myMiniTreeProducer.Trigger.bits.extend( egtriglist )
#process.myMiniTreeProducer.Trigger.bits.extend( jettriglist )
process.myMiniTreeProducer.Trigger.myTrig = "HLT_IsoMu"

process.myMiniTreeProducer.KineFit.runKineFitter = cms.bool(True)
process.myMiniTreeProducer.MCTruth.sampleChannel = cms.string('muon')
process.myMiniTreeProducer.Jets.resolutionsFile = cms.string('Spring16_25nsV10_MC_PtResolution_AK4PF.txt')
process.myMiniTreeProducer.Jets.scaleFactorsFile = cms.string('Spring16_25nsV10_MC_SF_AK4PF.txt')

#ANALYSIS SEQUENCE ------------------------------------------------------------
#Run without the KinFit
#process.p  = cms.Path(process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
#Run with the KinFit
process.p  = cms.Path(process.kinFitSequence*process.allEventsFilter*process.basePreSel*process.myMiniTreeProducer)
process.schedule = cms.Schedule(process.p)
checkProcessSchedule(storeOutPath,True)



#---------------------------- BACKUP ------------------------------------------
#Trigger POG: https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopTrigger#Summary_for_2016_Run2016B_H_25_n
#Trigger list: http://fwyzard.web.cern.ch/fwyzard/hlt/2016/summary
'''
mutriglist =  ['HLT_IsoMu24_v1',
               'HLT_IsoMu24_v2',
               'HLT_IsoMu24_v4',
               'HLT_IsoMu27_v3',
               'HLT_IsoMu27_v4',
               'HLT_IsoMu27_v5',
               'HLT_IsoMu27_v7']

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopTrigger?sortcol=3;table=4;up=0#sorted_table
egtriglist =  ['HLT_Ele27_WPTight_Gsf_v1',
               'HLT_Ele27_WPTight_Gsf_v2',
               'HLT_Ele27_WPTight_Gsf_v3',
               'HLT_Ele27_WPTight_Gsf_v4',
               'HLT_Ele27_WPTight_Gsf_v5',
               'HLT_Ele27_WPTight_Gsf_v6',
               'HLT_Ele27_WPTight_Gsf_v7',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v2',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v3',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v4',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v5',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v6',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v7',
               'HLT_Ele32_eta2p1_WPTight_Gsf_v8']

jettriglist = ['HLT_JetE30_NoBPTX_v2',
               'HLT_JetE30_NoBPTX_v3',
               'HLT_JetE30_NoBPTX_v4']
'''
#MG TT Jets
#inFile="/store/mc/RunIISummer16MiniAODv2/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/08BA365D-40E5-E611-955F-00266CF89498.root"

#inFile = "/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/002F2CE1-38BB-E611-AF9F-0242AC130005.root"

#inFile = "/store/mc/RunIISummer16MiniAODv2/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/042B8895-F6BF-E611-8DE4-70106F4A9340.root"

#inFile = "/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/120000/0EA60289-18C4-E611-8A8F-008CFA110AB4.root"
#inFile="/store/mc/RunIISummer16MiniAODv2/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/00450492-D4CB-E611-A0D1-0025904B5F96.root"

#inFile="/store/mc/RunIISummer16MiniAODv2/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0264D11E-24C0-E611-AFCB-24BE05CECB51.root"

#inFile = "/store/mc/RunIISummer16MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00E95BAA-C3D7-E611-A416-0025905A60BC.root"

#inFile = "/store/mc/RunIISummer16MiniAODv2/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/007FD85E-66B9-E611-AD58-0CC47A546E5E.root"
