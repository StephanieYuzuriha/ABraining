<template>
    <section>
      <p>Personal proyect by: Stephanie Marin</p>
     
      <div>
        <i class="fa fa-linkedin-square"></i>
        <a target="_blank" href="http://www.linkedin.com/in/stephanie-marin-guzman"> LinkedIn</a>
      </div>
      <div> 
        <i class="fa fa-github"></i>
        <a target="_blank" href="https://github.com/StephanieYuzuriha/Braining"> GitHub</a>
      </div> 
      <div>  
        <i class="fa fa-file-pdf-o"></i>
        <a href="@/assets/pdf/Maria Stephanie Marin Guzman.pdf" download> Curriculum</a>
      </div>
      
    </section>
    <p class="date">2022</p>
</template>

<script>
export default {
    name:"compFooter"

}
</script>

<style scoped>

section{
  display: flex;
  justify-content: center;
  flex-direction: column;

}
p{
  font-weight: bold;
}

.date{
  background-color: rgb(123, 58, 184);
}



</style>