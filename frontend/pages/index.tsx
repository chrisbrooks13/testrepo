// frontend/pages/index.tsx
// Home page for the Next.js app.
// Presents a simple UI example using a Lucide React icon.

import { FC } from 'react';
import { Rocket } from 'lucide-react';

const Home: FC = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Welcome to the AI SaaS Template</h1>
      <Rocket color="blue" size={48} />
    </div>
  );
};

export default Home;
