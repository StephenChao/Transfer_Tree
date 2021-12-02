'''
genH_pt
genH_eta
genH_phi
genH_mass
genH_w1_pt
genH_w1_eta
genH_w1_phi
genH_w1_mass
genH_w2_pt
genH_w2_eta
genH_w2_phi
genH_w2_mass
genH_w1_q1_pt
genH_w1_q1_eta
genH_w1_q1_phi
genH_w1_q1_mass
genH_w1_q1_pdg
genH_w1_q2_pt
genH_w1_q2_eta
genH_w1_q2_phi
genH_w1_q2_mass
genH_w1_q2_pdg
genH_w2_q1_pt
genH_w2_q1_eta
genH_w2_q1_phi
genH_w2_q1_mass
genH_w2_q1_pdg
genH_w2_q2_pt
genH_w2_q2_eta
genH_w2_q2_phi
genH_w2_q2_mass
genH_w2_q2_pdg
jetAK8puppi_pt
jetAK8puppi_eta
jetAK8puppi_phi
jetAK8puppi_sd
'''




AK8_Mode = '''
int AK8_Mode[2] = {-99};
// AK8_Mode[0] = 1, AK8 matched with higss
// AK8_Mode[0] = 2, AK8 matched with W
// AK8_Mode[0] = 3, AK8 matched with gq

//AK8_mode[0]=4, AK8 matched with 4q
//AK8_mode[0]=5, AK8 matched with 3q
//AK8_mode[0]=6, AK8 matched with lqq


// define fatJet 1,2
//cout<<"Nj8="<<Nj8<<endl;
TLorentzVector Genpart, Genpartd1, Genpartd2, Genpartd1d1, Genpartd1d2,Genpartd2d1, Genpartd2d2, fJ1, fJ2, fJ_pt1,fJ_pt2;
float deepWH_1,deepWH_2;

if(Nj8==1){
  fJ1.SetPtEtaPhiM(jetAK8puppi_pt, jetAK8puppi_eta, jetAK8puppi_phi, jetAK8puppi_sd );  
}

if(Nj8==2){



deepWH_1=(FatJetAK8_particleNet_H4qvsQCD+FatJetAK8_particleNetMD_Xqq+FatJetAK8_particleNetMD_Xcc)/(FatJetAK8_particleNet_H4qvsQCD+FatJetAK8_particleNetMD_Xqq+FatJetAK8_particleNetMD_Xcc+FatJetAK8_particleNetMD_QCD);
deepWH_2=(FatJetAK8_particleNet_H4qvsQCD_2+FatJetAK8_particleNetMD_Xqq_2+FatJetAK8_particleNetMD_Xcc_2)/(FatJetAK8_particleNet_H4qvsQCD_2+FatJetAK8_particleNetMD_Xqq_2+FatJetAK8_particleNetMD_Xcc_2+FatJetAK8_particleNetMD_QCD_2);


if(deepWH_1 > deepWH_2){
fJ1.SetPtEtaPhiM( jetAK8puppi_pt, jetAK8puppi_eta, jetAK8puppi_phi, jetAK8puppi_sd );
fJ2.SetPtEtaPhiM( jetAK8puppi_pt_2, jetAK8puppi_eta_2, jetAK8puppi_phi_2, jetAK8puppi_sd_2 );
}
if(deepWH_1 < deepWH_2){
fJ1.SetPtEtaPhiM( jetAK8puppi_pt_2, jetAK8puppi_eta_2, jetAK8puppi_phi_2, jetAK8puppi_sd_2 );
fJ2.SetPtEtaPhiM( jetAK8puppi_pt, jetAK8puppi_eta, jetAK8puppi_phi, jetAK8puppi_sd );
}

}



// define Gen particle, daughter1, daughter2
Genpart.SetPtEtaPhiM( genH_pt, genH_eta, genH_phi, genH_mass );
Genpartd1.SetPtEtaPhiM( genH_w1_pt, genH_w1_eta, genH_w1_phi, genH_w1_mass);
Genpartd2.SetPtEtaPhiM( genH_w2_pt, genH_w2_eta, genH_w2_phi, genH_w2_mass );
Genpartd1d1.SetPtEtaPhiM( genH_w1_q1_pt, genH_w1_q1_eta, genH_w1_q1_phi, genH_w1_q1_mass);
Genpartd1d2.SetPtEtaPhiM( genH_w1_q2_pt, genH_w1_q2_eta, genH_w1_q2_phi, genH_w1_q2_mass);
Genpartd2d1.SetPtEtaPhiM( genH_w2_q1_pt, genH_w2_q1_eta, genH_w2_q1_phi, genH_w2_q1_mass);
Genpartd2d2.SetPtEtaPhiM( genH_w2_q2_pt, genH_w2_q2_eta, genH_w2_q2_phi, genH_w2_q2_mass);

// match higgs
//cout<<"Genpart.DeltaR(fJ1) is:"<<fabs(Genpart.DeltaR(fJ1))<<endl;

if( fabs(Genpart.DeltaR(fJ1)) < 0.6 ){
    // AK8_Mode[0] = 1;
    // match W
    // cout<<"fabs(Genpartd1.DeltaR(fJ1)) is:"<<fabs(fabs(Genpartd1.DeltaR(fJ1)))<<endl;
    if( fabs(Genpartd1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd2.DeltaR(fJ1)) < 0.8 ){
        // AK8_Mode[0] = 2;
            if( (genH_w1_tag == 4) && (genH_w2_tag == 4)){
                if( fabs(Genpartd1d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd1d2.DeltaR(fJ1)) < 0.8 && fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd2d2.DeltaR(fJ1)) < 0.8 ){
                    AK8_Mode[0] = 4;
                }
                if( (fabs(Genpartd1d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd1d2.DeltaR(fJ1)) < 0.8)+ (fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd2d2.DeltaR(fJ1)) < 0.8)==1 ){
                    AK8_Mode[0] = 5;
                }
            }
            else{
                //One of the W decays leptonically
                // if w1 decays leptonically
                if(genH_w1_tag < 4){
                    // if w1 daughter1 is lepton
                    if(abs(genH_w1_q1_pdg)==11||abs(genH_w1_q1_pdg)==13||abs(genH_w1_q1_pdg)==15){
                        if( (fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8) && fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8){
                            AK8_Mode[0] = 6;
                        }
                    }
                    // if w1 daughter2 is lepton
                    if(abs(genH_w1_q2_pdg)==11||abs(genH_w1_q2_pdg)==13||abs(genH_w1_q2_pdg)==15){
                        if( (fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8) && fabs(Genpartd2d2.DeltaR(fJ1)) < 0.8){
                            AK8_Mode[0] = 6;
                        }
                    }                   
                }
                
                // if w2 decays leptonically
                if(genH_w2_tag < 4){
                    // if w2 daughter1 is lepton
                    if(abs(genH_w2_q1_pdg)==11||abs(genH_w2_q1_pdg)==13||abs(genH_w2_q1_pdg)==15){
                        if( (fabs(Genpartd1d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd1d1.DeltaR(fJ1)) < 0.8) && fabs(Genpartd2d1.DeltaR(fJ1)) < 0.8){
                            AK8_Mode[0] = 6;
                        }
                    }
                    // if w2 daughter2 is lepton
                    if(abs(genH_w2_q2_pdg)==11||abs(genH_w2_q2_pdg)==13||abs(genH_w2_q2_pdg)==15){
                        if( (fabs(Genpartd1d1.DeltaR(fJ1)) < 0.8 && fabs(Genpartd1d1.DeltaR(fJ1)) < 0.8) && fabs(Genpartd2d2.DeltaR(fJ1)) < 0.8){
                            AK8_Mode[0] = 6;
                        }
                    }                    
                }
                
            }    
    }
  //  cout<<"AK8_mode is"<<AK8_Mode[0]<<endl;
}

std::array <float, 2> AK8_Mode_arr;
for(size_t ik=0; ik<2;ik++){
    AK8_Mode_arr.at(ik) = AK8_Mode[ik];
}

return AK8_Mode_arr;
'''