int score(const int dice[5]) {
    int score = 0;
    int main_[10] = {0};
    for(int i = 0 ; i < 5 ; i++){
        main_[dice[i]] = main_[dice[i]] + 1;
        printf("%d = %d\n",dice[i],main_[dice[i]]);
    }

    
    if(main_[1] >= 3){
      score += 1000;
      main_[1] -= 3;
    }
    
    while(main_[1] > 0){
      main_[1] -= 1;
      score += 100;
    }
  
  printf("score after 1 : %d\n" , score);  
    
  
    for(int i = 2 ; i < 7 ; i++){
      if(main_[i] >= 3){
        score += ( i * 100 );
        main_[i] -= 3;
      }
    }  
    
    while(main_[5] > 0){
      main_[5] -= 1;
      score += 50;
    }
  printf("score = %d\n",score);
  return score;
  
}
