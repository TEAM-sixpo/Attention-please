import React from 'react';
import { ColumnMiddleContainer } from '../common/Containers';
import styled from 'styled-components';

const Logo = styled.img`
  width: 16rem;
  margin-bottom: 0.5rem;
`;

const P = styled.p`
  text-align: center;
  font-family: 'Pr-Regular';
  font-size: 0.85rem;
`;

const SignTitle = () => {
  return (
    <ColumnMiddleContainer>
      <Logo src="images/Logo.png" alt="Logo" />
      <P style={{ marginBottom: '3rem' }}>Be The center of Attention</P>
    </ColumnMiddleContainer>
  );
};

export default SignTitle;