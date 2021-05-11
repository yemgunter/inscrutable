class Techie:
  def __init__(self, first_name, last_name, job_title):
    self.first = first_name
    self.last = last_name
    self.title = job_title
    
  # create a function to return the Person's first name     
  def get_first(self):
    return self.first
    
  # create a function to return the Person's last name     
  def get_last(self):
    return self.last
    
  # create a function to return the Person's profession     
  def get_title(self):
    return self.title

def main():
    techie_list = []
    print('Enter data for two persons.')
    for count in range(1, 3):
        fname = input('Enter the first name: ')
        lname = input('Enter the last name: ')
        job = input('Enter the job title: ')
        print()
        
        techie = Techie(fname, lname, job)
        techie_list.append(techie)
        
    for techie in techie_list:
        print(techie.get_first(), '', end ='')
        print(techie.get_last())
        print(techie.get_title())
        print()
        
main()
