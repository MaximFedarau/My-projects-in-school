package main
import "fmt"
import "strconv"
func main() {
  var move string//move of player
  var a = [3][3]string{ {"-","-","-"},{"-","-","-"},{"-","-","-"}}//our gaming field
  var i,j int//valuables to get our field in rt mode
  var act=0
  for {
    if act==0 {
      for {// cycle need to get our field in real time
        if j==3 {
          fmt.Println(" ")
          j=0
          i++
        }
        if (i)==3 {
          break
        }
        fmt.Print(a[i][j]," ")
        j++
      }
      i = 0
      j = 0
    }
    fmt.Println("Choose a number from 1 to 9 or 'q' to exit the game.")//command to make different moves
    fmt.Scanln(&move)//reading player's moves
    if move=="q" {//if player wants to exit hte game
      fmt.Println("You exit the game!")
      break
    } else if move=="1" || move=="2" || move=="3" || move=="4" || move=="5" || move=="6" || move=="7" || move=="8" || move=="9" {//players moves
      move_1,err := strconv.Atoi(move)
      err = err
      var row int =0//we need to now the row
      if move_1%3==0 {
        row = move_1/3-1
      } else {
        row=move_1/3
      }
      var column int = 0//we need to know the column
      if move_1%3==0 {
        column = 2
      } else {
        column=move_1%3-1
      }
      var figure string//first player is cross, the second player is zero
      if act%2==0 {
        figure = "X"
      } else {
        figure = "O"
      }
      if a[row][column]=="-" {
        a[row][column]=figure
        act++
      } else {//if player want to put his sign in filled cell
        fmt.Println("Your input is incorrect. Try one more time!")
        act = act
      }
      for {// cycle need to get our field in real time
        if j==3 {
          fmt.Println(" ")
          j=0
          i++
        }
        if (i)==3 {
          break
        }
        fmt.Print(a[i][j]," ")
        j++
      }
      i = 0
      j = 0
      }else {//other input cases
        fmt.Println("Your command is wrong. Try one more time!")
        for {// cycle need to get our field in real time
          if j==3 {
            fmt.Println(" ")
            j=0
            i++
          }
          if (i)==3 {
            break
          }
          fmt.Print(a[i][j]," ")
          j++
        }
        i = 0
        j = 0
        continue
    }
    //if x-player won
    if (a[0][1]==a[0][0] && a[0][1]==a[0][2] && a[0][0]=="X") || (a[1][1]==a[1][0] && a[1][0]==a[1][2] && a[1][1]=="X") || (a[2][1]==a[2][0] && a[2][0]==a[2][2] && a[2][1]=="X") || (a[1][0]==a[0][0] && a[0][0]==a[2][0] && a[0][0]=="X") || (a[1][1]==a[0][1] && a[0][1]==a[2][1] && a[0][1]=="X") || (a[1][2]==a[0][2]&& a[0][2]==a[2][2] && a[2][2]=="X") || (a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[0][0]=="X") || (a[2][0]==a[1][1] && a[1][1]==a[0][2] && a[2][0]=="X") {
      fmt.Println("X-player won!!!")
      break
    }
    //if 0-player won
    if (a[0][1]==a[0][0] && a[0][1]==a[0][2] && a[0][0]=="O") || (a[1][1]==a[1][0] && a[1][0]==a[1][2] && a[1][1]=="O") || (a[2][1]==a[2][0] && a[2][0]==a[2][2] && a[2][1]=="O") || (a[1][0]==a[0][0] && a[0][0]==a[2][0] && a[0][0]=="O") || (a[1][1]==a[0][1] && a[0][1]==a[2][1] && a[0][1]=="O") || (a[1][2]==a[0][2]&& a[0][2]==a[2][2] && a[2][2]=="O") || (a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[0][0]=="O") || (a[2][0]==a[1][1] && a[1][1]==a[0][2] && a[2][0]=="O") {
      fmt.Println("O-player won!!!")
      break
    }
    var val_counter = 0// if x-player and 0-player both didn't win
    for {// cycle need to get our field in real time
      if j==3 {
        j=0
        i++
      }
      if (i)==3 {
        break
      }
      if a[i][j]!="-" {
        val_counter++
      }
      j++
    }
    i = 0
    j = 0
    if val_counter==9 {
      fmt.Println("Friendship won!!!")
      break
    }
    }
    }
