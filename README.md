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

#### _Υποερώτημα b_
* sim_seconds: 0.000035 (sec) Αναφέρεται στον συνολικό χρόνο προσομοίωσης σε δευτερόλεπτα. Είναι ένας δείκτης του συνολικού χρόνου που έχει παρέλθει κατά τη διάρκεια της προσομοίωσης.

* sim_insts: 5027(insts) Προσδιορίζει τον συνολικό αριθμό των εντολών (instructions) που εκτελέστηκαν κατά τη διάρκεια της προσομοίωσης. Είναι ένας μετρητής για τον συνολικό όγκο εργασίας που επιτελέστηκε από το σύστημα.

* host_inst_rate: 86201 (inst/sec) Προσδιορίζει το ρυθμό εκτέλεσης εντολών στον υπολογιστικό κόμβο (host) κατά τη διάρκεια της προσομοίωσης. Συνήθως μετριέται σε εντολές ανά δευτερόλεπτο και παρέχει πληροφορίες σχετικά με την απόδοση της προσομοίωσης σε επίπεδο υπολογιστικού κόμβου.

#### _Υποερώτημα c_
Βάσει του *stats.txt* συνολικά έχουμε 5028 committed instructions (_system.cpu_cluster.cpus.committedInsts_), ενώ 5831 commited ops (_system.cpu_cluster.cpus.committedOps_). Η διαφορά προκύπτει από το γεγονός ότι οι εντολές που στέλνονται προς τη CPU για εκτέλεση δεν έχουν 1-προς-1 αντιστοιχία με τα πραγματικά "micro-operations" που εκτελεί ο επεξεργαστής στο υλικό του. Με άλλα λόγια, μία εντολή από την ISA της CPU μπορεί να απαιτεί παραπάνω από ένα micro-operation για να εκτελεστεί.

#### _Υποερώτημα d_
Συνολικά η L2 cache προσπελάστηκε 474 φορές, όπως φαίνεται και από την καταχώρηση system.cpu_cluster.l2.overall_accesses::total 474   στο status.txt. Οι προσπελάσεις της L2 μπορούν να υπολογιστούν έμμεσα από τα misses της L1i L1d (dcache και icache): system.cpu_cluster.cpus.dcache.demand_mshr_misses::total  147 και system.cpu_cluster.cpus.icache.demand_misses::.cpu_cluster.cpus.inst  327. Σύνολο δηλαδή: 147 + 327 = 474


#### **Ερώτημα 3 - Βιβλιογραφική έρευνα**
Παρακάτω παραθέτω μια συνοπτική περιγραφή για ένα ακόμα μοντέλο:
1. MinorCPU:
    * Το MinorCPU είναι ένα in-order μοντέλο CPU που παρέχει υψηλή ακρίβεια στην προσομοίωση.
    * Υποστηρίζει εξελιγμένες λειτουργίες όπως ο speculative εκτελεστής και η προσομοίωση αποτυχιών.
    * Κατάλληλο για λεπτομερείς αναλύσεις απόδοσης.
2. SimpleCPU:
   * Το SimpleCPU είναι ένα απλό in-order μοντέλο CPU που προσφέρει βασική λειτουργικότητα για την προσομοίωση.
   * Δεν υποστηρίζει πολυνηματική εκτέλεση και είναι κατάλληλο για γρήγορες προσομοιώσεις.
3. AtomicSimpleCPU:
    * Το AtomicSimpleCPU είναι ένα in-order μοντέλο CPU που χρησιμοποιείται για απλές προσομοιώσεις.
    * Διαφέρει από το SimpleCPU στον τρόπο υλοποίησης του και παρέχει περιορισμένη λειτουργικότητα για την επίτευξη υψηλών επιδόσεων.
4. TimingSimpleCPU:
    * Το TimingSimpleCPU είναι ένα in-order μοντέλο CPU που προσομοιώνει τις καθυστερήσεις χρονισμού.
    * Χρησιμοποιείται για προσομοιώσεις που απαιτούν ακριβή μοντελοποίηση του χρονισμού εκτέλεσης.
  
  
#### _Υποερώτημα α_
|   | MinorCPU  | TimingSimpleCPU  |
|---|---|---|
|  Number of Ticks |  32204000 |  36631000  |
|  Simulation seconds   | 0.000032  |  0.000037  |
|  Number of CPU cycles | 64408  |  73262  | 
|  Number of committed instructions | 8442  |  8390  | 
|  CPI (cycles per instruction) |  7.6295  |  8.7321 |

#### _Υποερώτημα b_
Παρατηρούμε ότι ο _TimingSimpleCPU_ είναι κατά 15,63% πιο αργός από τον _MinorCPU_ για την εκτέλεση του ίδιου προγράμματος. Αυτή η διαφορά οφείλεται στο γεγονός ότι ο _TimingSimpleCPU_ δε διαθέτει κάποιο pipeline, ενώ επίσης λαμβάνει υπόψη του και τις καθυστερήσεις στο queueing των εντολών και μέσα στην cache, εκτός από αυτές που προκύπτουν αποκλειστικά λόγω της μεταφοράς δεδομένων από τη RAM στην cache.

#### _Υποερώτημα c_

### CPU clock: 100MHz
|   | MinorCPU  | TimingSimpleCPU  |
|---|---|---|
|  Number of Ticks |  171920000 |  285650000  |
|  Simulation seconds   | 0.000172  |  0.000286  |
|  Number of CPU cycles | 17192  |  28565  | 
|  Number of committed instructions | 8442  |  8390  | 
|  CPI (cycles per instruction) |  8.6783  |  3.4047 |

### Memory type: DDR4_2400_8x8
|   | MinorCPU  | TimingSimpleCPU  |
|---|---|---|
|  Number of Ticks |  30643000 |  36023000  |
|  Simulation seconds   | 0.000031  |  0.000036  |
|  Number of CPU cycles | 61286  |  72046  | 
|  Number of committed instructions | 8442  |  8390  | 
|  CPI (cycles per instruction) |  7.2597  |  8.5871 |

