const myChart = echarts.init(document.getElementById('radarchart'));

// 指定图表的配置项和数据
const option = {
  title: {
    text: ''
  },
  grid: {
    show: false,
    right: '30%',
    top: '30%',
    containLabel: true,
    bottom: '3%',
  },
  legend: {
    data: ['Allocated Budget', 'Actual Spending']
  },
  radar: {
    // shape: 'circle',
    indicator: [
      { name: '정확도', max: 5 },
      { name: '속도', max: 5 },
      { name: '세기', max: 5 },
      { name: '말 더듬', max: 5 },
      { name: '자세', max: 6 },
    ]
  },
  series: [
    {
      name: 'Budget vs spending',
      type: 'radar',
      data: [
        {
          value: [0, 0, 0, 0, 0],
          name: 'Actual Score'
        }
      ]
    }
  ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);

function Create_Achive () {
  const upload_file = document.getElementById('upload_file');
  const archiveRoute = upload_file.value;

  if (upload_file.files && upload_file.files[0]) {
    const viewfinder = new FileReader();

    viewfinder.onload = function(e) {
      document.getElementById('Visualize_archive').innerHTML= '<video controls id="button_video" src="'+e.target.result+'" width="519"></video>';
    }

    viewfinder.readAsDataURL(upload_file.files[0]);

    if (!archiveRoute) {
      alert('Select a VIDEO');
      upload_file.value = '';
      return false;
    } else {
      alert('Wait for the download of the video to play it');
    }
  }
}

const inputFile = document.querySelector('#upload_file');
inputFile.addEventListener('change', function () {
    let text = this.value;
    text = text.replace(/^.*\\/, "");
    document.getElementById("file_name").value = text;
});
