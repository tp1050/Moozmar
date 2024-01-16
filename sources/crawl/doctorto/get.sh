#a bash loop to curl the all 31 pages of the following url https://doctoreto.com/doctors/service/filler-injection?page=$X&sort=rate where x is the number of page and saves the html to file. with a a 2 second wait
# for i in {1..31}
# do
#     curl -s "https://doctoreto.com/doctors/service/filler-injection?page=$i&sort=rate" > "doctorto-$i.html"
#     sleep 2
# done



for i in {1..7582}
do
    curl -s "https://doctoreto.com/doctors?page=$i&sort=rate" > "assets/work/doctortoo-$i.html"
    sleep 2
done