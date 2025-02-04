const postsContainer = document.getElementById('resultado');

// Função para buscar todos os posts e exibir na tela
async function fetchPosts() {
  try {  
    // Pegar tds os posts e -> JSON
    const postsResponse = await fetch('https://jsonplaceholder.typicode.com/posts');
    const posts = await postsResponse.json();

    // LEMBRAR
    // {
    //     "userId": 1,
    //     "id": 1,
    //     "title": "delectus aut autem",
    //     "completed": false
    //   }

    
    // `https://jsonplaceholder.typicode.com/users/${post.userId}`
    //   {
    //     "id": 1,
    //     "name": "Leanne Graham",
    //     "username": "Bret",
    //     "email": "Sincere@april.biz",
    //     "address": {
    //       "street": "Kulas Light",
    //       "suite": "Apt. 556",
    //       "city": "Gwenborough",
    //       "zipcode": "92998-3874",
    //       "geo": {
    //         "lat": "-37.3159",
    //         "lng": "81.1496"
    //       }
    //     },
    //     "phone": "1-770-736-8031 x56442",
    //     "website": "hildegard.org",
    //     "company": {
    //       "name": "Romaguera-Crona",
    //       "catchPhrase": "Multi-layered client-server neural-net",
    //       "bs": "harness real-time e-markets"
    //     }
    //   }

    // Iteração
    for (const post of posts) {
    // ter a resposta do autor
      const userResponse = await fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`);
      const user = await userResponse.json();

      // Criar o elemento artigo
      const postElement = document.createElement('article');
      postElement.classList.add('post');
      postElement.innerHTML = `
        <h3>${post.title}</h3>
        <p>${post.body}</p>
        <p><strong>Autor:</strong> ${user.username} (${user.email})</p>
        <a href="#">Ver comentários</a>
      `;

      postsContainer.appendChild(postElement);
    }
  } catch (error) {
    console.error('Erro ao buscar posts:', error);
  }
}

fetchPosts();
