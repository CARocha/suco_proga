
    var chart_pie = {
         renderTo: 'container3',
         defaultSeriesType: 'pie',
         plotBackgroundColor: null,
         plotBorderWidth: null,
         plotShadow: false
      }

    var chart_column = {
        renderTo: 'container',
        defaultSeriesType: 'column'
    }
    
    var title = {
        text: ''
    }
    
    var subtitle = {
        text: ''
    } 
    var xAxis = {
        categories: [
                    'Opciones'
                ]
    }
    var yAxis = {
       min: 0,
       title: {
           text: ''
                }  
    }
    var tooltip = {
        formatter: function() {
                    return ''+
                        this.series.name +': '+ this.y +'%';
                }
    }
    var plotOptions = {
       column: {
                    groupPadding: 0,
                    pointPadding: 0.9,
                    borderWidth: 0
                },
                series: {
                    pointWidth: 55,
                    minPointLength : 1
                } 
    }            

