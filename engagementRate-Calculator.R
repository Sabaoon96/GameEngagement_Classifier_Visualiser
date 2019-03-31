#----------------------------------------------------------------------------------------------------------------------------
filesGTR = c(paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/0/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/1/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/2/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/3/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/4/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/5/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/Andon/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/Brad/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/Minha/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/Sabaoon/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/Shibani/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/Sindhu/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/GTR2/Tushar/0.csv"))

lapply(filesGTR, function(x) {
  
  GTRdata = read.csv(x)
  
  # Extracting columns and calculating engagement rate
  engagementGTR = (GTRdata['Low.Beta'] + GTRdata['High.Beta']) / (GTRdata['Theta'] + (GTRdata['Low.Alpha'] + GTRdata['High.Alpha']))
  # Averaging column data 
  avgGTR_eng = colMeans(engagementGTR)
  
})

#----------------------------------------------------------------------------------------------------------------------------

filesNFS = c(paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/0/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/1/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/2/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/3/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/4/0.csv"), 
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/5/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/Andon/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/Brad/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/Minha/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/Sabaoon/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/Shibani/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/Sindhu/0.csv"),
             paste0(getwd(), "/UserStudyData-JSON&CSV/NFS/Tushar/0.csv"))

lapply(filesNFS, function(x) {
  
  NFSdata = read.csv(x)
  
  # Extracting columns and calculating engagement rate
  engagementNFS = (NFSdata['Low.Beta'] + NFSdata['High.Beta']) / (NFSdata['Theta'] + (NFSdata['Low.Alpha'] + NFSdata['High.Alpha']))
  # Averaging column data 
  avgNFS_eng = colMeans(engagementNFS)
  
})


#----------------------------------------------------------------------------------------------------------------------------

filesBR = c(paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/0/0.csv"), 
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/1/0.csv"), 
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/2/0.csv"), 
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/3/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/4/0.csv"), 
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/5/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/Andon/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/Brad/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/Minha/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/Sabaoon/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/Shibani/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/Sindhu/0.csv"),
            paste0(getwd(), "/UserStudyData-JSON&CSV/BigRigs/Tushar/0.csv"))

lapply(filesBR, function(x) {
  
  BRdata = read.csv(x)
  
  # Extracting columns and calculating engagement rate
  engagementBR = (BRdata['Low.Beta'] + BRdata['High.Beta']) / (BRdata['Theta'] + (BRdata['Low.Alpha'] + BRdata['High.Alpha']))
  # Averaging column data 
  avgBR_eng = colMeans(engagementBR)
  
})
