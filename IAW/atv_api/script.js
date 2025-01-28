// API de Clima (OpenWeatherMap)
document.getElementById('weatherBtn').addEventListener('click', async () => {
    const apiKey = 'SUA_API'; // Substitua pela sua chave da API
    const city = document.getElementById('cidade').value.trim(); // Captura o nome da cidade
  
    if (!city) {
      document.getElementById('weatherOutput').textContent = 'Por favor, insira o nome da cidade.';
      return;
    }
  
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=pt`;
  
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Erro ao obter dados. Verifique o nome da cidade.');
      }
  
      const data = await response.json();
      const output = `
        <p>🌡️ Temperatura: ${data.main.temp}°C</p>
        <p>🌦️ Condições: ${data.weather[0].description}</p>
        <p>🌍 Cidade: ${data.name}, ${data.sys.country}</p>
      `;
      document.getElementById('weatherOutput').innerHTML = output;
    } catch (error) {
      document.getElementById('weatherOutput').textContent = error.message;
    }
  });
  
  // API de Usuário (ReqRes)
  document.getElementById('reqresBtn').addEventListener('click', async () => {
    const url = 'https://reqres.in/api/users';
    const payload = {
      name: 'Andressa',
      job: 'Desenvolvedora',
    };
  
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      const output = `
        <p>Usuário Criado: ${data.name}</p>
        <p>Cargo: ${data.job}</p>
        <p>ID: ${data.id}</p>
        <p>Criado em: ${data.createdAt}</p>
      `;
      document.getElementById('reqresOutput').innerHTML = output;
    } catch (error) {
      document.getElementById('reqresOutput').textContent = 'Erro ao criar usuário.';
    }
  });
  
  // API de Fatos sobre Gatos (Cat Facts)
  document.getElementById('catFactBtn').addEventListener('click', async () => {
    const url = 'https://catfact.ninja/fact';
  
    try {
      const response = await fetch(url);
      const data = await response.json();
      const output = `<p>${data.fact}</p>`;
      document.getElementById('catFactOutput').innerHTML = output;
    } catch (error) {
      document.getElementById('catFactOutput').textContent = 'Erro ao carregar dados.';
    }
  });
  