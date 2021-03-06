import FWCore.ParameterSet.Config as cms

import os,commands,time
def fillFrom(dirname):
    filelist = cms.untracked.vstring()
    for subdir, dirs, files in os.walk(dirname):
        for file in files:
            if(file.find('.root') == -1 ) : continue
            if(file.find('Monitor') != -1 ) : continue
            filelist.append('file:///'+dirname+'/'+file)
    return filelist

def mergeFileLists( fileListArray ):
    filelist = cms.untracked.vstring()
    for l in fileListArray :
        for f in l :
            filelist.append(f)
    return filelist

#data
dilcands = fillFrom('/lustre/lip.pt/data/cmslocal/pedros/DileptonCandidates2010')

#mc
ttbaraod=fillFrom('/lustre/lip.pt/data/cmslocal/pedros/TT1Jets-alpgen-aod')
ttbarRelVal384 = fillFrom('/lustre/lip.pt/data/cmslocal/pedros/RelVal_3_8_4/')
dyjetstoll = fillFrom('/lustre/lip.pt/data/cmslocal/pedros/Fall10/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/')
chhiggs = fillFrom('/lustre/lip.pt/data/cmslocal/nalmeida/mc/test/CMSSW_38X/HHtotaunu120/')
w2munu = fillFrom('/lustre/lip.pt/data/cmslocal/samples/CMSSW_3_8_6/w2MuNu')

#NICE WAY TO PRINT STRINGS
def toPrint(string, value):
    length = (len(string)+len(str(value))+2)
    line = "-"*length
    print ""
    print "* "+ line +                    " *"
    print "| "+ " "*length +              " |"
    print "| "+ string+ ": "+ str(value)+ " |"
    print "| "+ " "*length +              " |"
    print "* "+ line +                    " *"

#/////////////////////////////////////////////////////#
#   MC Samples of Charged Higgs & Bkg at 13 TeV       #
M = "/MINIAODSIM"
Year = "RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic"
HplusAllDataSets ={"TTJets": "/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+Year+"_v3-v3"+M,
        "TTJets_mtop169": "/TTJets_mtop1695_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+Year+"_v12-v1"+M,
        "TTJets_mtop175": "/TTJets_mtop1755_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+Year+"_v12-v1"+M,
        "ST_tW": "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+Year+"_v12-v1"+M,
        "ST_t": "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+Year+"_v12-v1"+M,
        "ST_s": "/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/"+Year+"_v12-v1"+M,
        "ST_tW": "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "W1JetsToLNu": "/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "W2JetsToLNu": "/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "W3JetsToLNu": "/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "W4JetsToLNu": "/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "DYJetsToLL": "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12_ext1-v1"+M,
        "DY1JetsToLL": "/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "DY2JetsToLL": "/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "DY3JetsToLL": "/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "DY4JetsToLL": "/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+Year+"_v12-v1"+M,
        "QCD_Pt-15to20_Mu": "/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+Year+"_v12-v1"+M,
        "WW": "/WW_TuneCUETP8M1_13TeV-pythia8/"+Year+"_v12-v1"+M,
        "WZ": "/WZ_TuneCUETP8M1_13TeV-pythia8/"+Year+"_v12-v1"+M,
        "ZZ": "/ZZ_TuneCUETP8M1_13TeV-pythia8/"+Year+"_v12-v1"+M,
        "QCD_Pt_30_80_EMEnriched":"",
        "QCD_Pt-15to20_EM": "/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+Year+"_v12-v1"+M,
        "QCD_Pt-120to170_EM": "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+Year+"_v12-v1"+M,
        "QCD_Pt-170to300_EM": "/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+Year+"_v12-v1"+M,
        "/TTToHplusBWB": ""
        }

#/////////////////////////////////////////////////////#





