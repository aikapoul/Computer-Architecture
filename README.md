# Αρχιτεκτονική Υπολογιστών ΑΠΘ 2023-2024
## _Πουλή Αικατερίνη, ΑΕΜ:7967, e-mail: aikapoul@ece.auth.gr_
### **ΜΕΡΟΣ ΠΡΩΤΟ**
#### **Ερώτημα 1**
Κοιτάζοντας το αρχείο **starter_se.py** εξάγουμε τα εξής δεδομένα:
* Τύπος CPU (CPU Type): AtomicSimpleCPU
* Συχνότητα CPU (CPU Frequency): 1GHz
* Αριθμός Πυρήνων CPU (Number of CPU Cores): 1
* Τύπος Μνήμης (Memory type): DDR3_1600_8x8
* Αριθμός Καναλιών Μνήμης (Number of Memory Channels): 2
* Αριθμός Ranks Μνήμης ανά Κανάλι (Number of Memory Ranks per Channel): None
* Φυσικό Μέγεθος Μνήμης (Physical Memory Size): 2GB
* Τάση συστήματος (VoltageDomain): 3.3V
  
#### **Ερώτημα 2**
#### _Υποερώτημα α_
Όσον αφορά τα αρχεία **_config.ini_** και **_config.json_** εξάγουν τα ίδια αποτελέσματα με διαφορετική μορφή. Για ευκολία χρησιμοποιείται το **_config.ini_** και εξάγονται τα εξής:
* Τύπος CPU: Minor (type=MinorCPU)
* Συχνότητα CPU: 1Ghz (clock=1000)
* Αριθμός Πυρήνων CPU:1 (numThreads=1)
* Τύπος Μνήμης: DDR3_1600_8x8 (Μετά από ψάξιμο στα config)
* Αριθμός Καναλιών Μνήμης: 2 (system.mem_ctrls0 & system.mem_ctrls1)
* Αριθμός Ranks Μνήμης ανά Κανάλι: 2 (ranks_per_channel=2 για κάθε module)
* Φυσικό Μέγεθος Μνήμης: 2GB (mem_ranges=0:2147483647/1024*1024)
* Τάση συστήματος: 3.3V (voltage=3.3)
* Σχετικά με τους caches: Έχουμε L1d και L1i για δεδομένα και εντολές αντίστοιχα[2], L2 και walkcache. To L1d (dcache) έχει μέγεθος 32768 = 32 KB (size=32768) και το L1i 49152 = 48KB size=49152. Το walker_cache έχει μέγεθος 1ΚΒ (size=1024) και το L2 1MB (size=1048576).
