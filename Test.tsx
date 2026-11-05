import React from "react";

const awsToken: string = "AKIALALEMEL33243OKIA";

export default function TestComponent(): JSX.Element {
    return <div data-aws-token={awsToken}>Gitleaks test fixture</div>;
}
