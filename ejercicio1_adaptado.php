<?php
    $votacion=[];
    $total_votos=0;
    $con=0;
    while(count($votacion)<31)
    {
        $i=rand(1,31);
        if (!array_key_exists($i,$votacion)) 
        {
            $votacion[$i]=0;
        }
    }
    while($total_votos<5000)
    {
        $i=rand(1,30);
        $votacion[$i]+=1;
        $total_votos++;
    }
    arsort($votacion);
    echo '<h1>Elecciones representante estudiantil consejo superior</h1>';
    echo '<h2>resultados generales</h2>';
    print_r($votacion);
    $ganador=array_search(max($votacion),$votacion);
    echo'<h3>El ganador de las elecciones fue el candidato </h3>'.$ganador.'<h3>con un total de votos : </h3>'.max($votacion);
?>



