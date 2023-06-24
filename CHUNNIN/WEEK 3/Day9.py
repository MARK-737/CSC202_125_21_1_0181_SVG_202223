#PYTHON DICTIONARY


student_scores={
"Harry": 81,
"Ron":78,
"Herione":99,
"Draco":74,
"Neville":62,

}


student_grades={}
  
for student in student_scores:
    score=student_scores[student]
    if score>90:
     student_grades[student] ="Outstanding"
    elif score>80:
        student_grades[student]="Exceeds Expectation" 
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"
        
print("student_grades") 



#NESTED DICTIONARY

capitals={"france": "Paris", "Germany": "Berling",} 
    
    
    ##NESTLING DICTIONARY IN A DICTIONARY
    
travel_log={
     "france": {"cities_visited":["paris", "lille", "dijon"], "total_visits":12}, "germany":["berlin", "hamburg", "stuttgart"],
                    
 }      




##NESTLING DICTIONARY IN A LIST



travel_log=[
     {
         "country": "france",
         "visits":12,
         "cities":["paris", "lille", "dijon"]
      }, 
     {
         "country": "germany",
         "visits":5,
         "cities": ["berlin", "hamburg", "stuttgart"]
         },
        
]


def add_new_country(country_visited, times_visited, cities_visited):
 new_country={}
 new_country["country"]=country_visited
 new_country["visits"]=times_visited
 new_country["cities"]=cities_visited 
 travel_log.append(new_country)   
 
 
 
 add_new_country("russia", 2, ["Moscow", "Saint Petersbourg"])
 print(travel_log)
 
 
 
#blind-auction
bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
 highest_bid=0
 
 #bidding_record={"Angela": 123, }
 for bidder in bidding_record:
  bid_amount=bidding_record[bidder]
  if   bid_amount> highest_bid:
      highest_bid=bid_amount
      winner=bidder
      print(f"The winner is {winner} with a bid of ${highest_bid}")
      
while not bidding_finished:
 name=input("what is your name?") 
 price=int(input("what is ypur bid? $"))
 bids[name]=price
 should_continue=input("Are there any other bidders? Type 'yes' or 'no' ")
 if should_continue=="no":
     bidding_finished =True
     find_highest_bidder(bids)
 elif should_continue=="yes":
  print() 